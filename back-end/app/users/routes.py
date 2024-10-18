from app.users import users_bp
from flask import jsonify, make_response, request
from app.extensions import db
from app.models.users import Users
from flask_login import login_user, logout_user, login_required

@users_bp.route('/login', methods=['POST'])
def login():
    loginRequest = request.get_json()
    email = loginRequest['email']
    password = loginRequest['password']
    user = Users.query.filter_by(email=email).first()
    # if user and user.check_password(password):
    if user and user.password == password:
        login_user(user)
        return make_response(jsonify(user.serialize), 200)
    else:
        return make_response('Incorrect email or password', 401)


@users_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return make_response('Success', 200)


@users_bp.route('/register', methods=['POST'])
def register():
    # 1- Take json body inside an object
    # 2- check if email already exists
    # 3- check if password and confrim are the same
    # 4- create Users model object
    # 5- save this model using db session add
    # 6- commit the changes
    # 7- return users model with 201 code 

    userDTO = request.get_json()
    user_email = Users.query.filter_by(email=userDTO["email"]).first()
    if user_email is not None:
         return make_response('Email already exists', 400)
    if(userDTO["password"]!=userDTO["confirm_password"]):
         return make_response('Passwords should be the same', 400)
    
    user = Users(userDTO["username"],userDTO["password"],userDTO["email"],userDTO["full_name"])
    db.session.add(user)
    db.session.commit()
    return make_response(jsonify(user.serialize), 200)
