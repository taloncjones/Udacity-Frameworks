from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Output menu of restaurant specified by /restaurant/<id>/ path
@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    output = ""
    for i in items:
        output += "%s<br>" % i.name
        output += "%s<br>" % i.price
        output += "%s<br>" % i.description
        output += "<br>"
    return output

# Task 1: Create route for newMenuItem function here

def newMenuItem(restaurant_id):
    return "Page to create a new menu item. Task 1 complete!"


# Task 2: Create route for editMenuItem function here

def editMenuItem(restaurant_id, menu_id):
    return "Page to edit a menu item. Task 2 complete!"


# Task 3: Create route for deleteMenuItem function here

def deleteMenuItem(restaruant_id, menu_id):
    return "Page to delete a menu item. Task 3 complete!"


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8080)
