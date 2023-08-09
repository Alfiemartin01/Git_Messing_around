from application import db
from flask_wtf import FlaskForm
from wtforms import SelectField,IntegerField,StringField,SubmitField

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prod_name = db.Column(db.String(30), nullable=False)
    product = db.relationship('Order_Product',backref='productbr') #used to define relationships between tables
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_name = db.Column(db.String(30), nullable=False)
    order = db.relationship('Order_Product',backref='orderbr') #used to define relationships between tables
class Order_Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), default="Athena")
    order_id = db.Column(db.Integer,db.ForeignKey('order.id'), nullable=False)
    prod_id = db.Column(db.Integer,db.ForeignKey('product.id'), nullable=False)

class Person(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    hair_col = db.Column(db.String)
class PersonForm(FlaskForm): #Creates a form
    name = StringField("Name: ") #creates a string input field
    age = IntegerField("Age: ")
    hair_col = SelectField("Breed: ",choices=[('Brown','Brown'),('Blonde','Blonde')]) #sleectfield stores the first word chosen, and displays the second to the user as the choice
    submit = SubmitField("Submit")
