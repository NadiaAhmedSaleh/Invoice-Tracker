
from flask import jsonify, make_response, request , render_template, redirect, url_for
from app.invoices import invoices_bp
from app.models.invoice import Invoice
from app.extensions import db
from datetime import datetime
from flask_login import login_required , current_user
from sqlalchemy import and_ 
from pathlib import Path
import os.path

#List invoices
@invoices_bp.route('/list', methods=['GET'])
@login_required
def list():
   status_arg = request.args.get('status') 
    ##select all from invoices where current_user.id == user_id
    ##select all from invoices where status = paid and user_id =4
   if status_arg is None or status_arg == "":
      invoices = Invoice.query.filter_by(user_id=current_user.id)
   else: 
      invoices = Invoice.query.filter(and_(Invoice.user_id == current_user.id , Invoice.status == status_arg)) 
   return render_template('homePage.html', invoices=invoices)
   
     
#Create invoice#

@invoices_bp.route('/add', methods=['GET','POST'])
@login_required
def add():
    # Input: Json object thats exactly look like Invoice object
   if request.method == 'POST':
      invoice = Invoice(**request.form)
      invoice.date_issued = datetime.strptime(invoice.date_issued, "%Y-%m-%d").date()
      invoice.due_date = datetime.strptime(invoice.due_date, "%Y-%m-%d").date()
      invoice.status = 'Pending'
      invoice.user_id = current_user.id
      db.session.add(invoice)
      db.session.commit()
   
      return redirect(url_for("home"))

   else:
      return render_template("addInvoice.html")
 


#Delete invoice
@invoices_bp.route('/delete/<id>' , methods=['DELETE'])
@login_required
def delete(id):
   invoice = Invoice.query.get(id)
   # - open the file
   
   # - add a new line in the file with invoice.serialize() 
   # - close the file 
   #- print(invoice.serialize)
   if current_user.id == invoice.user_id:
      if invoice.status=="Paid":  
         history_file = open(str(current_user.id) + ".txt", "a+" )
         history_file.write(str(invoice.serialize) + "\n")   
         history_file.close()
         db.session.delete(invoice)
         db.session.commit()
        
         return make_response("successfully changed" , 200)
      else:
         return render_template('homePage.html', msg="Can't delete this item unless it's marked as paid")
   else:
      return render_template('homePage.html', msg="unauthorized")

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
       # return redirect(url_for('invoices.list'), code=303)
       return make_response("successfully changed" , 200)
    else:
       return make_response("you can't change this" , 400)   
 else:
      return make_response("unauthorized", 401)

# q- Input: Json object of invoice  - PUT
# OutPut: return Updated invoice obj with 200   
#update invoice

#Edit an invoice
@invoices_bp.route('/update', methods=['GET','POST' ])
@login_required
def update():
   
   if request.method == 'POST': 
      
      invoice = Invoice(**request.form)
      invoice_bp=Invoice.query.get(invoice.id)
      if current_user.id==invoice_bp.user_id: 
         invoice_bp.date_issued = datetime.strptime(invoice.date_issued, "%Y-%m-%d").date()
         invoice_bp.due_date = datetime.strptime(invoice.due_date, "%Y-%m-%d").date()
         
         invoice_bp.issuer=invoice.issuer
         invoice_bp.amount=invoice.amount

         db.session.commit()
         return redirect(url_for("home"))
      else: 
         return render_template("editInvoice.html" , msg="error")
   else:
      id_arg = request.args.get('id') 
      invoice = Invoice.query.get(id_arg)
      return render_template("editInvoice.html" , invoice=invoice)
 
# 1- GET   -> HTML
# post aw put -> form -> home


##read from txt file 
## write it into the new html page
## would the same function send the user to the html page and then read from txt file??
@invoices_bp.route("/history", methods=['GET'])
@login_required
def get_history():
   history = []
   filename = str(current_user.id) + ".txt"
   if Path.is_file(filename):
      invoice_history_file=open(filename)
      content=invoice_history_file.read()
      invoice_history_file.close()
      history=content.split("\n")
   return render_template("history.html" , invoice_history=history)


##read from txt file 
## write it into the new html page
## would the same function send the user to the html page and then read from txt file??
@invoices_bp.route("/old-invoices", methods=['GET'])
@login_required
def get_old_invoices():
   history = []
   filepath =  Path('../../' + str(current_user.id))
   if not (filepath.is_file()):
      filename = str(current_user.id) + ".txt"
      invoice_history_file=open(filename)
      content=invoice_history_file.read()
      invoice_history_file.close()
      history=content.split("\n")
   return render_template("history.html" , invoice_history=content)
