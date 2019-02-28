Welcome to my implementation of the Restaurant Menu/Restaurant Database project from Udacity.
This program's intended purpose is to keep a database of restaurants and their menus, while
providing a user-friendly webpage to navigate the database. The main objectives of this
course were:
 - Allow the user to navigate a database of restaurants and their menus
 - Allow the user to add, edit, or remove restaurants
 - Allow the user to add, edit, or remove restaurant menu items
 - Add API calls for: a list of restaurants, a restaurant's menu, a particular menu item
 - Display html pages in a user-friendly manner by adding css

Anything with '-final' in the file name was made as part of the final project (with the
exception of finalproject.py and README.md). The others were either supplied or based off of
Udacity course lessons (with some personalization).

## Initialize the database with:
```python database_setup.py```

## (Optional) Populate the database with values:
Note: These values were provided by the Udacity course\
```python lotsofmenus.py```

## Run the web server with:
```python finalproject.py```
#### Or to detach it:
```python finalproject.py &```

## JSON
Responses can be requested from the following paths:
#### RestaurantList: (Lists all restaurants in the database)
```
/JSON/
or
/restaurants/JSON/
```
#### Menu: (Lists all menu items for restaurant supplied by <rest_id>)
```
/restaurants/<int:rest_id>/JSON/
or
/restaurants/<int:rest_id>/menu/JSON/
```
#### Item: (Lists details of a single menu item supplied by <item_id>)
```
/restaurants/<int:rest_id>/<int:item_id>/JSON/
or
/restaurants/<int:rest_id>/menu/<int:item_id>/JSON/
```

## Steps for dependencies:
```
## Install dependencies.
apt-get -qqy install make zip unzip postgresql

apt-get -qqy install python3 python3-pip
pip3 install --upgrade pip
pip3 install flask packaging oauth2client redis passlib flask-httpauth
pip3 install sqlalchemy flask-sqlalchemy psycopg2-binary bleach requests

apt-get -qqy install python python-pip
pip2 install --upgrade pip
pip2 install flask packaging oauth2client redis passlib flask-httpauth
pip2 install sqlalchemy flask-sqlalchemy psycopg2-binary bleach requests
```
