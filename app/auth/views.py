from flask import render_template,flash, request, redirect, url_for
from flask_login import login_user, logout_user,login_required
from app.auth import auth
from app.models import User
from .forms import RegForm,LoginForm
from ..email import mail_message

@auth.route('/login',methods = ['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user != None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Wrong Username or Password')
    return render_template('auth/login.html',form = form)

@auth.route('/signup',methods = ["POST","GET"])
def signup():
    form = RegForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email = form.email.data, password=form.password.data)
        user.save()
        flash('Your account has been created! You are now able to login','success')
        msg = Message(subject="The Creek", sender="testingemailpk6@gmail.com", recipients=[user.email])
        msg.body = f"Hello "+ user.username.capitalize()+", Welcome to the creek, We have just seen you have signed up for our application and want to welcome you to the family. Please enjoy."
        mail.send(msg)
        return  redirect(url_for('auth.login'))
    return render_template('auth/signup.html',registration_form=form )

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
    