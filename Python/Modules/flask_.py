from flask import Flask
from random import randint
firstname = ['Alice','Athena','Abigail','April','Autumn']
lastname =  ['Smith','Green','Martin','Swift']

app = Flask(__name__)


@app.route('/')
def index():
    return (f'{firstname[randint(0,len(firstname)-1)]} {lastname[randint(0,len(lastname)-1)]}')
    
app.run()