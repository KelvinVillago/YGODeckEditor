from . import api
from app import db
from app.models import Phone
from flask import request
from .auth import basic_auth

@api.route('/token')
def get_token():
    auth_user = basic_auth.current_user()
    token = auth_user.get_token()
    return {'token':token,
            'token_expiration': auth_user.token_expiration}

@api.route('/posts')
def get_nums():
    nums = db.session.execute(db.select(Phone)).scalars().all()
    return [num.to_dict() for num in nums]

@api.route('/posts/<post_id>')
def get_num(num_id):
    num = db.session.get(Phone, num_id)
    if num:
        return num.to_dict()
    else:
        return {'error': f'Post with an ID of {num_id} does not exist'}, 404

@api.route('/posts', methods=["POST"])
def create_post():
    print(request)
    # Check to see that the request body is JSON
    if not request.is_json:
        return {'error': 'Your content-type must be application/json'}, 400
    # Get the data from the request body
    data = request.json
    print(data)

    required_fields = ['first_name','last_name', 'address', 'phoneNum']
    missing_fields = []
    for field in required_fields:
        if field not in data:
            missing_fields.append(field)
    if missing_fields:
        return {'error': f"{', '.join(missing_fields)} must be in the request body"}
    
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    address = data.get('address')
    phoneNum = data.get('phoneNum')

    #create new post
    newNum = Phone(first_name=first_name, last_name=last_name, address=address, phoneNum=phoneNum, user_id=current_user.id)


    return 'This is the create phone number route'