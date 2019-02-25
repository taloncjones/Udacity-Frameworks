#!/usr/bin/env python
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem


app = Flask(__name__)


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
