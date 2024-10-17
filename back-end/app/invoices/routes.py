
from flask import jsonify, make_response, request 
from app.invoices import invoices_bp
from app.models.invoice import Invoice
from app.extensions import db
from datetime import datetime
from flask_login import login_required , current_user


#List invoices

@invoices_bp.route('/list', methods=['GET'])
# @login_required
def list():
    status_arg = request.args.get('status')
    invoice = Invoice(**request.get_json())

    if current_user.id == invoice.user_id:
       if status_arg is None:
        invoices = Invoice.query.all()
       else: invoices = Invoice.query.filter_by(status=status_arg)
       return make_response(jsonify(invoices=[i.serialize for i in invoices]), 200)
    else:
       return make_response("unauthorized" , 401)
#Create invoice#

@invoices_bp.route('/add', methods=['POST'])
#@login_required
def add():
    # Input: Json object thats exactly look like Invoice object
    invoice = Invoice(**request.get_json())

    invoice.date_issued = datetime.strptime(invoice.date_issued, "%Y-%m-%d").date()
    invoice.due_date = datetime.strptime(invoice.due_date, "%Y-%m-%d").date()
    if(current_user.id != invoice.user_id):
        return make_response ("Unaouthorized", 401)
    else:
     db.session.add(invoice)
     db.session.commit()
     return make_response(jsonify(invoice.serialize), 201)
 


#Delete invoice
@invoices_bp.route('/delete/<id>' , methods=['DELETE'])
@login_required
def delete(id):
   invoice = Invoice.query.get(id)
   # - open el file
   # - add a new line in the file with invoice.serialize() 
   # - close the file 

   if current_user.id == invoice.user_id:
     if invoice.status=="Paid":
        history_file = open("invoicesHistory.txt")
        history_file.write(invoice.serialize())
        history_file.close()
        db.session.delete(invoice)
        db.session.commit()
        return make_response("Success", 200)
     else:
        return make_response("Can't delete this item unless it's marked as paid", 400)
   else:
      return make_response("unauthorized", 401)

# q- Input: Path Var called id    - PUT
# OutPut:  if status = pending set -> Paid then return Updated invoice obj with 200   
#  else return 400 with message error its already paid 
##mark as paid

#Mark as paid
@invoices_bp.route('/mark-as-paid/<id>' , methods=['PUT'])
@login_required
def mark_as_paid(id):
 invoice=Invoice.query.get(id)
    
 if current_user.id == invoice.user_id: 
    if invoice.status=="Pending":
       invoice.status="Paid"
       db.session.commit()
       return make_response(jsonify(invoice.serialize), 200)
    else:
       return make_response("you can't change this" , 400)   
 else:
      return make_response("unauthorized", 401)

# q- Input: Json object of invoice  - PUT
# OutPut: return Updated invoice obj with 200   
#update invoice

#Edit an invoice
@invoices_bp.route('/update', methods=['PUT'])
@login_required
def update():
    invoice = Invoice(**request.get_json())
    if current_user.id==invoice.user_id:
     invoice.date_issued = datetime.strptime(invoice.date_issued, "%Y-%m-%d").date()
     invoice.due_date = datetime.strptime(invoice.due_date, "%Y-%m-%d").date()

     db.session.merge(invoice)
     db.session.flush()
     db.session.commit()
     return make_response(jsonify(invoice.serialize), 200)
    else:
       return make_response("unauthorized" , 401)




##read from txt file 
## write it into the new html page
## would the same function send the user to the html page and then read from txt file??
def get_history(): 
 invoices_history=open("invoicesHistory.txt")
 content=invoices_history.read()
 invoices_history.close()
 history=content.split("\n")
 return history


##goes to the html file and retrieve data from txt file 

def history():
   html_page = open("history.html")
   history_invoice=get_history()
   actual_values=""
   for history in history_invoice:
        actual_values += "<p>" + history + "</p>"
   return html_page.replace("$$GUESTS$$" , actual_values)  

