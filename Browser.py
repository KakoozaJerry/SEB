from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Daily import Base, Daily, Shop

app = Flask(__name__)

engine = create_engine('sqlite:///shop.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# @app.route('/')
# @app.route('/vw')
# def view():
#      return "Hurray!!!"

@app.route('/')
@app.route('/sales/<int:shop_i>/')
def saleMenu(shop_i):
    restaurant = session.query(Shop).filter_by(id=shop_i).one()
    items = session.query(Daily).filter_by(shop_id=shop_i).all()
#    return redirect(url_for('deleteMenuItem' , shop_id = shop_i))
#    return jsonify(Shops=[i.serialize for i in items])
#    return redirect(url_for('deleteMenuItem', shop_id=shop_i)
    return render_template('menu.html', restaurant=restaurant, items=items)


# @app.route('/sales/<int:sales_i>/new/')
# def newItem(sales_i, menu_id):
#     return "page to edit a menu item. Task 2 complete!"

# @property
# def serialize(self):
#     return {
#         'name' : self.name,
#         'id' : self.id,
#         'price' : self.price,
#         'item' : self.item,
#     }
#     output = ''
#     for i in items:
#         output += i.name
#         output += '</br>'
#         output += i.price
#         output += '</br>'
#         output += i.item
#         output += '</br>'
#         output += '</br>'
#     return output
#     return render_template('menu.html', restaurant=restaurant, items=items)


@app.route('/sales/<int:shop_id>/create/')
def newEntry(shop_id):
    return "page to add a new Entry. Task 1 complete!"

@app.route('/sales/<int:shop_id>/edit/')
def editEntry(shop_id):
    return "page to edit a menu item. Task 2 complete!"

@app.route('/sales/<int:shop_id>/delete/')
def deleteEntry(shop_id):
    return "page to delete a menu item. Task 3 complete!"


# @app.route('/sales/<int:sale_i>/new/', methods=['GET', 'POST'])
# def newEntry(sale_i):
#     if request.method == 'POST':
#         newItem = Daily(name=request.form['name'], restaurant_id= sale_i)
#         session.add(newItem)
#         session.commit()
#         return redirect(url_for('saleMenu', restaurant_id= sale_i))
#     else:
#         return render_template('editmenuitem.html', restaurant_id= sale_i)
#


if __name__ == '__main__':
    #app.secret_key = 'super_secret_key'
    # app.debug = True
    app.run()
