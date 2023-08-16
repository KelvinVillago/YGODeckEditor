from app import app, db
from flask import render_template, redirect, url_for
from app.forms import AddContact
from app.models import User


#add a route
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/addcontact', methods=["GET", "POST"])
def addContact():
    form = AddContact()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        phoneNum = form.phoneNum.data
        address = form.address.data
        
        #create new user
        newUser = User(first_name=first_name, last_name=last_name, phoneNum=phoneNum, address=address)
        
        #add user to database
        db.session.add(newUser)
        db.session.commit()

        #return to home page
        return redirect(url_for('index'))

    return render_template('addcontact.html', form=form)