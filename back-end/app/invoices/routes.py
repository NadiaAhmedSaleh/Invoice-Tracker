
from flask import jsonify, make_response, request , render_template, redirect, url_for
from app.invoices import invoices_bp
from app.models.invoice import Invoice
from app.extensions import db
from datetime import datetime
from flask_login import login_required , current_user
from sqlalchemy import and_ 
from pathlib import Path
import os.path


#check on status
#check on user id
#get invoices of that specific user and display it in homepage
#filter by status if the user entered a status

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
   


#if method is post 
# render the add.html page
# add invoices data and automatically set status to pending
# add data to db and commit
# then redeirect to homepage     
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
 

#get invoice with the same id sent in the parameter
#check if the status is paid 
#delete the invoice from db 
#open file and write in it

#Delete invoice
@invoices_bp.route('/delete/<id>' , methods=['DELETE'])
@login_required
def delete(id):
   invoice = Invoice.query.get(id)
   # - open a new file if the user doesn't have one or append to an exisiting one
   # - write the invoice in the file
   # - close the file 
   
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


#check on the status
#if the status is pending 
#then change it to paid
# then commit changes 

#Mark as paid
@invoices_bp.route('/mark-as-paid/<id>' , methods=['PUT'])
@login_required
def mark_as_paid(id):
 invoice=Invoice.query.get(id)
    
 if current_user.id == invoice.user_id: 
    if invoice.status=="Pending":
       invoice.status="Paid"
       db.session.commit()
       
       return make_response("successfully changed" , 200)
    else:
       return make_response("you can't change this" , 400)   
 else:
      return make_response("unauthorized", 401)

 
#get the needed to change invoice
#edit it
#commit to db

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
 



##read from txt file 
## write it into the new html page
#render the history.html page

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
