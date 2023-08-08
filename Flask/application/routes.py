
from application import app, db
from application.models import *
from flask import render_template,request,redirect


@app.route('/') #runs when the url end point matches
def main():
    return render_template('index.html', name='Athena') #displays index.html

@app.route('/form' methods=["GET","POST"])
def form():
    form = PersonForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            person = Person(
                name = form.name.data,
                age = form.age.data,
                hair_col = form.hair_col.data
            ) 
            db.session.add(person)
            db.session.commit()
    return render_template('form.html', form=form)

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

   # prod1 = Product(prod_name='prod1')
   # db.session.add(prod1)
   # 
    #prod2 = Product(prod_name='prod2')
    #db.session.add(prod2)
    #order1 = Order(order_name='Martin')
    #db.session.add(order1)
    #

#    order_prod1 = Order_Product(first_name='Athena', orderbr=order1,productbr=prod1)
#    db.session.add(order_prod1)
#    db.session.commit()