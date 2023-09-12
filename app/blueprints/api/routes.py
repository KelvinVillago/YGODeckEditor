from . import api
from app import db
from app.models import Deck, User
from flask import request
from .auth import basic_auth, token_auth

@api.route('/token')
@basic_auth.login_required
def get_token():
    auth_user = basic_auth.current_user()
    token = auth_user.get_token()
    return {'token':token,
            'token_expiration': auth_user.token_expiration}

@api.route('/users')
def get_users():
    nums = db.session.execute(db.select(User)).scalars().all()
    return [num.to_dict() for num in nums]

@api.route('/decks')
def get_decks():
    nums = db.session.execute(db.select(Deck)).scalars().all()
    return [num.to_dict() for num in nums]

@api.route('/decks/<num_id>')
def get_num(num_id):
    num = db.session.get(Deck, num_id)
    if num:
        return num.to_dict()
    else:
        return {'error': f'Deck with an ID of {num_id} does not exist'}, 404

@api.route('decks', methods=["POST"])
@token_auth.login_required
def create_deck():
    print(request)
    # Check to see that the request body is JSON
    if not request.is_json:
        return {'error': 'Your content-type must be application/json'}, 400
    # Get the data from the request body
    data = request.json
    print(data)

    required_fields = ['name', 'mainDeck','extraDeck', 'sideDeck']
    missing_fields = []
    for field in required_fields:
        if field not in data:
            missing_fields.append(field)
    if missing_fields:
        return {'error': f"{', '.join(missing_fields)} must be in the request body"}
    
    name = data.get('name')
    mainDeck = data.get('mainDeck')
    sideDeck = data.get('sideDeck')
    extraDeck = data.get('extraDeck')

    current_user = token_auth.current_user()

    newDeck = Deck(name=name, mainDeck=mainDeck, extraDeck=extraDeck, sideDeck=sideDeck, user_id=current_user.id)

    db.session.add(newDeck)
    db.session.commit()

    return newDeck.to_dict(), 201

@api.route('/decks/<num_id>', methods=['PUT'])
@token_auth.login_required
def edit_deck(num_id):
    # Check to see that the request body is JSON
    if not request.is_json:
        return {'error': 'Your content-type must be application/json'}, 400
    deck = db.session.get(Deck, num_id)
    if deck is None:
        return{'error':f"Deck with id {num_id} does not exist"}, 404
    #make sure authenticated user is deck author
    current_user = token_auth.current_user()
    if deck.user_id != current_user.id:
        return {'error': 'You do not have permission to edit this deck'}, 403     
    data = request.json
    for field in data:
        if field in {'name', 'mainDeck','extraDeck', 'sideDeck'}:
            setattr(deck, field, data[field])

    db.session.commit()
    return deck.to_dict()

@api.route('/decks/<num_id>', methods=['DELETE'])
@token_auth.login_required
def delete_deck(num_id):
    # Check to see that the request body is JSON
    if not request.is_json:
        return {'error': 'Your content-type must be application/json'}, 400
    deck = db.session.get(Deck, num_id)
    if deck is None:
        return{'error':f"Deck with id {num_id} does not exist"}, 404
    #make sure authenticated user is deck author
    current_user = token_auth.current_user()
    if deck.user_id != current_user:
        return {'error': 'You do not have permission to edit this deck'}, 403         
    db.session.delete()
    db.session.commit()
    return {'success':f"{deck.title} has been deleted"}

@api.route('/users/me')
@token_auth.login_required
def get_self():
    me = token_auth.current_user()
    return me.to_dict()

@api.route('/users/me', methods=['DELETE'])
@token_auth.login_required
def delete_user(num_id):
    me = token_auth.current_user()

    if(me is None):
        return {'error', 'You do not have permission to delete this user'}

    # Check to see that the request body is JSON
    if not request.is_json:
        return {'error': 'Your content-type must be application/json'}, 400
    user = db.session.get(User, me)
    if user is None:
        return{'error':f"User does not exist"}, 404
    
    db.session.delete()
    db.session.commit()
    return {'success':f"{user.username} has been deleted"}

@api.route('/users/me', methods=['PUT'])
@token_auth.login_required
def edit_user(num_id):
    me = token_auth.current_user()
    
    if (me is None):
        return {'error': 'You do not have permission to edit this user'}, 403   

    # Check to see that the request body is JSON
    if not request.is_json:
        return {'error': 'Your content-type must be application/json'}, 400
    user = db.session.get(User, me)
    if user is None:
        return{'error':f"User does not exist"}, 404
      
    data = request.json
    for field in data:
        if field in {'firstName', 'lastName','username', 'password', 'email'}:
            setattr(user, field, data[field])

    db.session.commit()
    return user.to_dict()
