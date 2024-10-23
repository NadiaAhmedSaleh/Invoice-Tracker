from flask import Flask, render_template ,redirect , url_for
from config import Config
from app.extensions import db
from flask_login import LoginManager, current_user
from flask_bcrypt import Bcrypt
from flask_cors import CORS

login_manager = LoginManager()


def create_app(configirations=Config):
    app = Flask(__name__)
  
    CORS(app)
    app.config.from_object(configirations)
    db.init_app(app)
    bcrypt = Bcrypt(app)
    login_manager.init_app(app)
    from app.invoices import invoices_bp
    app.register_blueprint(invoices_bp, url_prefix='/invoices')
    from app.users import users_bp
    app.register_blueprint(users_bp, url_prefix='/users')
    
    @app.route('/')
    @app.route('/home')
    def home():
        if current_user.is_anonymous:
            return redirect(url_for('users.login'))
        return redirect(url_for('invoices.list'))
        
    return app
