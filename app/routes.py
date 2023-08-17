from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm, AddContact, LoginForm
from app.models import User, Phone
from flask_login import login_user, logout_user, login_required, current_user

#add a route
@app.route('/')
def index():
    nums = db.session.execute(db.select(Phone)).scalars().all()
    return render_template('index.html', nums=nums)

@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        print(first_name, last_name, username, email, password)
        
        #check user table to see if any users with username or email
        checkUser = db.session.execute(db.select(User).where( (User.username==username) | (User.email==email))).scalar()
        if checkUser:
            flash('A user with that password already exists')
            return redirect(url_for('signup'))

        #create new user
        newUser = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        
        #add user to database
        db.session.add(newUser)
        db.session.commit()

        flash(f'{newUser.username} has been created')

        #login user
        login_user(newUser)

        #return to home page
        return redirect(url_for('index'))

    return render_template('signup.html', form=form)

@app.route('/logout')
@login_required
def logout():
    flash('You have successfully logged out')
    logout_user()
    return redirect(url_for('index'))

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        # Query the User table for a user with that username
        user = db.session.execute(db.select(User).where(User.username==username)).scalar()
        # If we have a user AND the password is correct for that user
        if user is not None and user.check_password(password):
            # log the user in via login_user function
            login_user(user)
            flash('You have successfully logged in')
            return redirect(url_for('index'))
        else:
            flash('Invalid username and\or password')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)


@app.route('/addcontact', methods=["GET", "POST"])
@login_required
def addContact():
    form = AddContact()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        phoneNum = form.phoneNum.data
        address = form.address.data
        
        #create new user
        newUser = Phone(first_name=first_name, last_name=last_name, phoneNum=phoneNum, address=address, user_id=current_user.id)
        
        #add user to database
        db.session.add(newUser)
        db.session.commit()

        #return to home page
        return redirect(url_for('index'))

    return render_template('addcontact.html', form=form)