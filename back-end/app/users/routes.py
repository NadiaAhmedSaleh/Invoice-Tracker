from app.users import users_bp
from flask import jsonify, make_response, request, render_template , redirect , url_for
from app.extensions import db
from app.models.users import Users
from flask_login import login_user, logout_user, login_required, current_user

#check if user is already logged in then render his home
#if not then check on email and password from front
#get the user that has the same email 
#check on its password
#if all good then log in and render his home
#if not good then render the login page again


#login

@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        user = Users.query.filter_by(email=email).first()
        # if user and user.check_password(password):
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('home', user=user))
        else:
            return render_template('login.html', error='Incorrect email or password')
    else:
        return render_template('login.html')


#you have to be logged in to logout
#if not redirect to login page

#logout

@users_bp.route('/logout')
@login_required
def logout():
    if current_user is not None:
        logout_user()
    return redirect(url_for('users.login'))



# 1- Take json body inside an object
# 2- check if email already exists
# 3- check if password and confrim are the same
# 4- create Users model object
# 5- save this model using db session add
# 6- commit the changes
# 7- return homepage 

#register 

@users_bp.route('/register', methods=['GET', 'POST'])
def register():
   
    if current_user.is_authenticated:
        return redirect(url_for('home'))
        
    userDTO = request.form
    if request.method == 'POST' and 'email' in userDTO:
        user_email = Users.query.filter_by(email=userDTO["email"]).first()
        if user_email is not None:
            return render_template('signup.html', error='Email already exists')
        if(userDTO["password"]!=userDTO["confirm_password"]):
            return render_template('signup.html', error='Passwords should be the same')

        user = Users(userDTO["username"],userDTO["password"],userDTO["email"],userDTO["full_name"])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home', user=user))
    else:
        return render_template('signup.html')


