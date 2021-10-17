from market import app
from flask import render_template
from market.models import Item

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html',items=items)

@app.route('/login')
def login_page(username):
    return f'<h1>this is the about page of {username}</h1>'

@app.route('/register')
def register_page():
    return '<h1>About page</h1>'