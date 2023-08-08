#from os import getenv
from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) #Creates a Flask object
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

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



@app.route('/') #runs when the url end point matches
def main():
    return("Ping -------- Pong --------- Ping --------- Pong")

@app.route('/post')
def post():
    return(request.method)

@app.route('/google')
def google():
    return redirect('http://www.google.com')

###### Routes Exercise
@app.route('/<int:num>')
def squared(num:int) -> int:
    return(f'{num**2}')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) #runs the app in debug mode

