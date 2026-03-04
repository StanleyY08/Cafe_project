from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

DATABASE = "Cafe_database"

app = Flask(__name__)

def connect_database(db_file):
    """
    creates a connection with the database
    :param db_file:
    :return: conn
    """
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
        print(f'An error occurred when connecting to the database. ')
    return None


@app.route('/')
def render_homepage():
    return render_template('home.html')


@app.route('/menu/<cat_id>')
def render_menu(cat_id):
    con = connect_database(DATABASE)
    query = "SELECT name, description, volume, image, price FROM products WHERE fk_cat_id=?"
    query_cat_list = "SELECT * FROM categories"
    cur = con.cursor()
    cur.execute(query, (cat_id,))
    product_list = cur.fetchall()
    cur.execute(query_cat_list)
    cat_list = cur.fetchall()
    print(product_list)
    print(cat_list)
    con.close()
    return render_template('menu.html', list_of_coffees = product_list, list_of_catergories=cat_list)


@app.route('/contact')
def render_contact_page():
    return render_template('contact.html')


app.run(host='0.0.0.0', debug=True)
