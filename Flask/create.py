from application import app,db


with app.app_context():
    db.drop_all() #removes all the data from the databse
    db.create_all() #inserts all data into database

    prod1 = Product(prod_name='prod1')
    db.session.add(prod1)
    
    prod2 = Product(prod_name='prod2')
    db.session.add(prod2)
    order1 = Order(order_name='Martin')
    db.session.add(order1)
    

    order_prod1 = Order_Product(first_name='Athena', orderbr=order1,productbr=prod1)
    db.session.add(order_prod1)
    db.session.commit()