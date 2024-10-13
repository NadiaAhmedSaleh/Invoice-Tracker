from flask import Flask
from config import Config
from app.extensions import db


def create_app(configirations=Config):
    app = Flask(__name__)
    app.config.from_object(configirations)
    db.init_app(app)


    from app.invoices import invoices_bp
    app.register_blueprint(invoices_bp, url_prefix='/invoices')

    return app

