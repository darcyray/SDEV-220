from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello!'

@app.route('/books')
def get_books():
    
    return {"books": "book_data"}