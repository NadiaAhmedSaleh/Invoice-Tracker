from flask import Blueprint
invoices_bp = Blueprint('invoices', __name__)

from app.invoices import routes


#made a blueprint for the invoices