from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    last_name = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    
    favorites = db.relationship("Favorites", backref="user", lazy=True)

    
    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "name": self.name,
            "last_name":self.last_name,
            "email":self.email,
            "password":self.password,
            "is_active":self.is_active,
            "characters":self.characters,
            "location":self.planets,
            "favorites":self.favorities

     
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    status = db.Column(db.String(80), unique=False, nullable=False)
    especies = db.Column(db.Boolean(), unique=False, nullable=False)
    type_ = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(80), unique=False, nullable=False)
    origin = db.Column(db.String(80), unique=False, nullable=False)
    location = db.Column(db.String(80), unique=False, nullable=False)
    url = db.Column(db.String(120), unique=True, nullable=False)
    created = db.Column(db.String(80), unique=False, nullable=False)
    favorites = db.relationship("Favorites", backref="characters", lazy=True)
 
    def __repr__(self):
        return '<Characters %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "status":self.status,
            "especies":self.especies,
            "type_":self.type_,
            "gender":self.gender,
            "origin":self.origin,
            "location":self.location,
            "url":self.url,
            "created":self.created

     
            # do not serialize the password, its a security breach
        }
    
   
class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    type_ = db.Column(db.String(120), unique=True, nullable=False)
    dimension = db.Column(db.String(80), unique=False, nullable=False)
    residents = db.Column(db.String(80), unique=False, nullable=False)
    url = db.Column(db.String(120), unique=True, nullable=False)
    created = db.Column(db.String(80), unique=False, nullable=False)
    favorites = db.relationship("Favorites", backref="location", lazy=True)


    def __repr__(self):
        return '<Location %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "type_":self.type_,
            "dimension":self.dimension,
            "residents":self.residents,
            "url":self.url,
            "created":self.created

     
            # do not serialize the password, its a security breach
        }
class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"),nullable=False)
    characters_id = db.Column(db.Integer, db.ForeignKey("characters.id"))
    location_id = db.Column(db.Integer,db.ForeignKey("location.id"))
   


    def __repr__(self):
        return '<favorites %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "Characters_id":self.characters_id,
            "Location_id":self.location_id
        
            # do not serialize the password, its a security breach
        }

    
    


    
    

