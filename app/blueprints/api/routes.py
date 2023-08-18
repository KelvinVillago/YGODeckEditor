from . import api
from app import db
from app.models import Phone
from flask import request
from .auth import basic_auth, token_auth

@api.route('/token')
def get_token():
    auth_user = basic_auth.current_user()
    token = auth_user.get_token()
    return {'token':token,
            'token_expiration': auth_user.token_expiration}

@api.route('/phone_nums')
def get_nums():
    nums = db.session.execute(db.select(Phone)).scalars().all()
    return [num.to_dict() for num in nums]

@api.route('/phone_nums/<num_id>')
def get_num(num_id):
    num = db.session.get(Phone, num_id)
    if num:
        return num.to_dict()
    else:
        return {'error': f'phone with an ID of {num_id} does not exist'}, 404

@api.route('/phone_nums', methods=["POST"])
def create_num():
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

    #create new phone
    newNum = Phone(first_name=first_name, last_name=last_name, address=address, phoneNum=phoneNum, user_id=current_user.id)

    return 'This is the create phone number route'

@api.route('/phone_nums/<num_id>', methods=['PUT'])
@token_auth.login_required
def edit_num(num_id):
    # Check to see that the request body is JSON
    if not request.is_json:
        return {'error': 'Your content-type must be application/json'}, 400
    phone = db.session.get(Phone, num_id)
    if phone is None:
        return{'error':f"Phone with id {num_id} does not exist"}, 404
    #make sure authenticated user is phone author
    current_user = token_auth.current_user()
    if phone.user_id != current_user:
        return {'error': 'You do not have permission to edit this phone'}, 403     
    data = request.json
    for field in data:
        if field in {'first_name', 'last_name', 'address', 'phone_number'}:
            setattr(phone, field, data[field])

    db.session.commit()
    return phone.to_dict()

@api.route('/phone_nums/<num_id>', methods=['DELETE'])
@token_auth.login_required
def delete_num(num_id):
    # Check to see that the request body is JSON
    if not request.is_json:
        return {'error': 'Your content-type must be application/json'}, 400
    phone = db.session.get(Phone, num_id)
    if phone is None:
        return{'error':f"Phone with id {num_id} does not exist"}, 404
    #make sure authenticated user is phone author
    current_user = token_auth.current_user()
    if phone.user_id != current_user:
        return {'error': 'You do not have permission to edit this phone'}, 403         
    db.session.delete()
    db.session.commit()
    return {'success':f"{phone.title} has been deleted"}