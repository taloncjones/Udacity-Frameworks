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
    return "List of restaurants"

# Route for adding a new restaurant
@app.route('/restaurants/new/')
def newRestaurant():
    return "New restaurant"

# Route for editing a restaurant
@app.route('/restaurants/<int:rest_id>/edit/')
def editRestaurant(rest_id):
    return "Edit restaurant %s" % rest_id

# Route for deleting a restaurant
@app.route('/restaurants/<int:rest_id>/delete/')
def deleteRestaurant(rest_id):
    return "Delete restaurant %s" % rest_id

# Routes for restaurant menu specified by <rest_id>
@app.route('/restaurants/<int:rest_id>/')
@app.route('/restaurants/<int:rest_id>/menu/')
def restaurantMenu(rest_id):
    return "Menu for restaurant %s" % rest_id

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
