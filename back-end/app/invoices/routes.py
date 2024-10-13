
from flask import jsonify, make_response, request
from app.invoices import invoices_bp
from app.models.invoice import Invoice
from app.extensions import db
from datetime import datetime


# Ways to pass data to an API
# 1- Path var /delete/<id>
# 2- Body request.get_json()
# 3- Path params request.args.get('status')


@invoices_bp.route('/list', methods=['GET'])
def list():
    status_arg = request.args.get('status')
    if status_arg is None:
        invoices = Invoice.query.all()
    else:
        invoices = Invoice.query.filter_by(status=status_arg)
    return make_response(jsonify(invoices=[i.serialize for i in invoices]), 200)


@invoices_bp.route('/add', methods=['POST'])
def add():
    # Input: Json object thats exactly look like Invoice object
    invoice = Invoice(**request.get_json())
    invoice.date_issued = datetime.strptime(invoice.date_issued, "%Y-%m-%d").date()
    invoice.due_date = datetime.strptime(invoice.due_date, "%Y-%m-%d").date()

    db.session.add(invoice)
    db.session.commit()
    return make_response(jsonify(invoice.serialize), 201)


@invoices_bp.route('/delete/<id>' , methods=['DELETE'])
def delete(id):
   invoice = Invoice.query.get(id)
   if invoice.status=="Paid":
        db.session.delete(invoice)
        db.session.commit()
        return make_response("Success", 200)
   else:
        return make_response("Can't delete this item unless it's marked as paid", 400)

# q- Input: Path Var called id    - PUT
# OutPut:  if status = pending set -> Paid then return Updated invoice obj with 200   
#  else return 400 with message error its already paid 
##mark as paid

@invoices_bp.route('/mark-as-paid/<id>' , methods=['PUT'])
def mark_as_paid(id):
    invoice=Invoice.query.get(id)
    if invoice.status=="Pending":
        invoice.status="Paid"
        db.session.commit()
        return make_response(jsonify(invoice.serialize), 200)
    
    else:
        return make_response("it's already paid", 400)
    
# q- Input: Json object of invoice  - PUT
# OutPut: return Updated invoice obj with 200   


