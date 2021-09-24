import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Characters,  Planets, Vehicles, Favorites 
from flask_migrate import Migrate
#from flask_script import Manager

BASEDIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(BASEDIR, "test.db") 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
#manager = Manager(app)
db.init_app(app)
Migrate(app, db)

@app.route('/')
def home():
    return jsonify('Star Wars API')

@app.route("/user", methods=["POST", "GET"])

def user():
    if request.method == "GET":
        user = User.query.all()
        user = list(map(lambda user: user.serialize(), user))
        if user is not None:
            return jsonify(user)
    else:
        user = User()
        user.username = request.json.get("username")
        user.first_name = request.json.get("first_name")
        user.last_name = request.json.get("last_name")
        user.password = request.json.get("password")
        user.email = request.json.get("email")
        
        
        db.session.add(user)
        db.session.commit()

        return jsonify(user.serialize()), 200


@app.route("/planets", methods=["POST", "GET"])
def planets():
    if request.method == "GET":
        planets = Planets.query.all()
        planets = list(map(lambda planets: planets.serialize(), planets))
        if planets is not None:
            return jsonify(planets)
    else:
        planets = Planets()
        planets.name = request.json.get("name")
        planets.climate = request.json.get("climate")
        planets.terrain = request.json.get("terrain")
        planets.diameter = request.json.get("diameter")
        
        db.session.add(planets)
        db.session.commit()

        return jsonify(planets.serialize()), 200



@app.route("/characters", methods=["POST", "GET"])

def characters():
    if request.method == "GET":
        characters = Characters.query.all()
        characters = list(map(lambda characters: characters.serialize(), characters))
        if characters is not None:
            return jsonify(characters)
    else:
        characters = Characters()
        characters.name = request.json.get("name")
        characters.mass = request.json.get("mass")
        characters.eye_color = request.json.get("eye_color")
        characters.gender = request.json.get("gender")

        db.session.add(characters)
        db.session.commit()

        return jsonify(characters.serialize()), 200


@app.route("/vehicles", methods=["POST", "GET"])

def vehicles():
    if request.method == "GET":
        vehicles = Vehicles.query.all()
        vehicles = list(map(lambda vehicles: vehicles.serialize(), vehicles))
        if vehicles is not None:
            return jsonify(vehicles)
    else:
        vehicles = Vehicles()
        vehicles.name = request.json.get("name")
        vehicles.model = request.json.get("model")
        vehicles.cargo_capacity = request.json.get("cargo_capacity")
        vehicles.vehicle_class = request.json.get("vehicle_class")

        db.session.add(vehicles)
        db.session.commit()

        return jsonify(vehicles.serialize()), 200

@app.route("/favorites", methods=["POST", "GET"])

def favorites():
    if request.method == "GET":
        favorites = Favorites.query.all()
        favorites = list(map(lambda favorites: favorites.serialize(), favorites))
        if favorites is not None:
            return jsonify(favorites)
    else:
        favorites = Favorites()
        favorites.user_id = request.json.get("user_id")
        favorites.planets_id = request.json.get("planets_id")
        favorites.characters_id = request.json.get("characters_id")
        favorites.vehicles_id  = request.json.get("vehicles_id")

        db.session.add(favorites)
        db.session.commit()

        return jsonify(favorites.serialize()), 200





if __name__ == "__main__":
    app.run(host='localhost', port=8080)