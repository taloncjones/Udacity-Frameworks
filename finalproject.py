#!/usr/bin/env python

# finalproject.py for Udacity Course 3 created by Talon Jones
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem


app = Flask(__name__)


# Setup and bind db session
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


### Routes for finalproject.py go here
# Routes for main menu (list of restaurants)
@app.route('/')
@app.route('/restaurants/')
def allRestaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants=restaurants)

# Route for adding a new restaurant
@app.route('/restaurants/new/', methods=['GET', 'POST'])
def newRestaurant():
    if request.method == 'POST':
        newRest = Restaurant(name=request.form['name'])
        session.add(newRest)
        session.commit()
        return redirect(url_for('allRestaurants'))
    else:
        return render_template('newrestaurant.html')

# Route for editing a restaurant
@app.route('/restaurants/<int:rest_id>/edit/', methods=['GET', 'POST'])
def editRestaurant(rest_id):
    editRest = session.query(Restaurant).filter_by(id=rest_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editRest.name = request.form['name']
        session.add(editRest)
        session.commit()
        return redirect(url_for('allRestaurants'))
    else:
        return render_template('editrestaurant.html', rest=editRest)

# Route for deleting a restaurant
@app.route('/restaurants/<int:rest_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(rest_id):
    deleteRest = session.query(Restaurant).filter_by(id=rest_id).one()
    if request.method == 'POST':
        session.delete(deleteRest)
        session.commit()
        return redirect(url_for('allRestaurants'))
    else:
        return render_template('deleterestaurant.html', rest=deleteRest)

# Routes for restaurant menu specified by <rest_id>
@app.route('/restaurants/<int:rest_id>/')
@app.route('/restaurants/<int:rest_id>/menu/')
def restaurantMenu(rest_id):
    restaurant = session.query(Restaurant).filter_by(id=rest_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=rest_id).all()
    return render_template('menu-final.html', rest=restaurant, items=items)

# Route for adding a new restaurant menu item
@app.route('/restaurants/<int:rest_id>/new/')
def newMenuItem(rest_id):
    return "New menu item for restaurant %s" % rest_id

# Route for editing a restaurant menu item
@app.route('/restaurants/<int:rest_id>/<int:item_id>/edit/')
def editMenuItem(rest_id, item_id):
    return "Edit menu item %s" % item_id

# Route for deleting a restaurant menu item
@app.route('/restaurants/<int:rest_id>/<int:item_id>/delete/')
def deleteMenuItem(rest_id, item_id):
    return "Delete menu item %s" % item_id

# Run if called by file finalproject.py
if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
