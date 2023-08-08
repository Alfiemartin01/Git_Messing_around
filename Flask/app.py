#from os import getenv
from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) #Creates a Flask object
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/pythondb'
db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), default="Athena")
    last_name = db.Column(db.String(30), unique=True)
    alive = db.Column(db.Boolean, nullable=False)
    datetime = db.Column(db.DateTime)

new_user = Person(first_name='Athena',last_name='Martin',alive=True)

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

