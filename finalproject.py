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

# Route for adding a new restaurant
@app.route('/restaurants/new/')

# Route for editing a restaurant
@app.route('/restaurants/<int:rest_id>/edit/')

# Route for deleting a restaurant
@app.route('/restaurants/<int:rest_id>/delete/')

# Routes for restaurant menu specified by <rest_id>
@app.route('/restaurants/<int:rest_id>/')
@app.route('/restaurants/<int:rest_id>/menu/')

# Route for adding a new restaurant menu item
@app.route('/restaurants/<int:rest_id>/new/')

# Route for editing a restaurant menu item
@app.route('/restaurants/<int:rest_id>/<int:item_id>/edit/')

# Route for deleting a restaurant menu item
@app.route('/restaurants/<int:rest_id>/<int:item_id>/delete/')

# Run if called by file finalproject.py
if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
