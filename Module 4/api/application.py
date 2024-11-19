from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(8))
    description = db.Column(db.String(120))

@app.route('/')
def index():
    return 'Hello!'

@app.route('/books')
def get_books():
    
    return {"books": "book_data"}

