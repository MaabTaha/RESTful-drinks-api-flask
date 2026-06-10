# everytime you open a new terminal (use GitBash) run:
# make sure you are in api folder
#   export FLASK_APP=application.py
#   export FLASK_ENV=development
#   flask run
# get the web link and paste into browser, example: "http://127.0.0.1:5000"

# in terminal (GitBash)
# run "python"
# run "from application import app, db"
# not needed anymore to run this (it's added to this file already): "app.app_context().push()""
# db.create_all()
# from application import Drink
# drink = Drink(name="Grape Soda", description="Tastes like grapes")
# db.session.add(drink)
# db.session.commit()

# OR use inline method of adding drink:

# db.session.add(Drink(name="Mango Smoothie", description="heavy milky icy piece of heaven!"))
# db.session.commit()
# to end, run "exit()""


# some methods require the use of Postman namely: 
# POST (add drink) and DELETE (drink)

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
app.app_context().push()


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"

@app.route('/')
def index():
    return 'Hello!'

@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()

    output = []
    for drink in drinks:
        drink_data = {'name': drink.name, 'description': drink.description}
        output.append(drink_data)
    return {"drinks":output}

@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return jsonify({"name":drink.name, "description": drink.description}) # no need to 
# jsonify with dicts but might be needed for other data types

@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id':drink.id}
# To test in Postman:
# POST http://127.0.0.1:5000/drinks/3
# Body:
# {
#     "name": "Mango Tea",
#     "description": "hot drink"
# }


@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {"error": "not found"}
    db.session.delete(drink)
    db.session.commit()
    return {"message": "successfully deleted"}

# To test in Postman:
# DELETE http://127.0.0.1:5000/drinks/3
# Body:
# empty
