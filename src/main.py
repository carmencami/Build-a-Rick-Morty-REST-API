"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Location, Favorites

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():
    userDb = User.query.all()
    userlist = list(map(lambda obj : obj.serialize(),userDb))
    print(userlist)

    response_body = {
        "success" : True,
        "result": "userlist"
    }

    return jsonify(response_body), 200

@app.route('/user', methods=['POST'])
def add_User():

    body = json.loads(request.data)

    newUser = User(email = body["email"], password = body ["password"], is_active = True)
    db.session.add(newUser)
    db.session.commit()
    print(body)
    response_body = {
        "succes" : True,
        "result": "Creado"
    }

    return jsonify(response_body), 200

@app.route('/character', methods=['PUT'])
def character_user():

    body = json.loads(request.data)

    newUser = User(email = body["email"], password = body ["password"], is_active = True)
    db.session.add(newUser)
    db.session.commit()
    print(body)
    response_body = {
        "succes" : True,
        "result": "Creado"
    }

    return jsonify(response_body), 200

@app.route('/characters', methods=['GET'])
def characters():
    characters=Characters.query.all()
    all_characters= list(map(lambda characters : characters.serialize(),characters))
    return jsonify(all_characters)

@app.route('/character/<int:id>', methods=['GET'])
def character(id):
    character=Characters.query.get(id)
    return jsonify(character.serialize())

@app.route('/location', methods=['GET'])
def locations():
    location=Location.query.all()
    all_location= list(map(lambda location : location.serialize(),location))
    return jsonify(all_location)

@app.route('/location/<int:id>', methods=['GET'])
def location(id):
    location=Location.query.get(id)
    return jsonify(location.serialize())

@app.route('/favorites/user/<int:user_id>/characters/<int:characters_id>', methods=['POST'])
def add_favorites_characters(user_id,characters_id):

    newFavorite = Favorites(user_id= user_id, characters_id = characters_id)
    db.session.add(newFavorite)
    db.session.commit()
    response_body = {
        "succes" : True,
        "result": "Creado", 
        "favorites":newFavorite.serialize()
    }

    return jsonify(response_body), 200

@app.route('/favorites/user/<int:user_id>/location/<int:location_id>', methods=['POST'])
def add_favorites_locations(user_id,location_id):

    newFavorite = Favorites(user_id= user_id, location_id = location_id)
    db.session.add(newFavorite)
    db.session.commit()
    response_body = {
        "succes" : True,
        "result": "Creado", 
        "favorites":newFavorite.serialize()
    }

    return jsonify(response_body), 200

@app.route('/favorites/user/<int:user_id>/location/<int:location_id>', methods=['DELETE'])
def delete_favorites_locations(user_id,location_id):
    favorites=Favorites.query.filter_by(user_id=user_id).filter_by(location_id=location_id).first()

    db.session.delete(favorites)
    db.session.commit()
    response_body = {
        "succes" : True,
        "result": "Borrado", 
    }

    return jsonify(response_body), 200

@app.route('/favorites/user/<int:user_id>/characters/<int:characters_id>', methods=['DELETE'])
def delete_favorites_characters(user_id,characters_id):
    favorites=Favorites.query.filter_by(user_id=user_id).filter_by(characters_id=characters_id).first()

    db.session.delete(favorites)
    db.session.commit()
    response_body = {
        "succes" : True,
        "result": "Borrado", 
    }

    return jsonify(response_body), 200


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)



