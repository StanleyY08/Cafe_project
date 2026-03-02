from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

DATABASE = "Cafe_database"

app = Flask(__name__)


@app.route('/')
def render_homepage():
    return render_template('home.html')


@app.route('/menu')
def render_menu():
    return render_template('menu.html')


@app.route('/contact')
def render_contact_page():
    return render_template('contact.html')


app.run(host='0.0.0.0', debug=True)
