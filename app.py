import json,os,flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True
    

if os.path.exists("books.json"):
        books = json.load(open("books.json"))
else:
    print("file not found") 
@app.route('/', methods=['GET'])
def home():
    return '''<h1> PROJET : api </h1> <h2> Utilisation des méthodes GET, POST, PUT, DELETE </h2>'''

@app.route('/api/books', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/books/<int:id>', methods=['GET'])
def api_id(id):
    book = [book for book in books if book['id']==id]
    return jsonify({"books":book})

@app.route('/api/books/delete/<int:id>',methods=['DELETE'])
def api_delete(id):
    book = [book for book in books if book['id']== id]
    books.remove(book[0])
    return jsonify({'books:':books})

@app.route('/api/books/add',methods=['POST'])
def post():
    user = request.get_json()
    user['id'] = len(books)+1
    books.append(user)
    return jsonify(user)

@app.route('/api/books/update',methods=['PUT'])
def put():
    user = request.get_json()
    for i,u in enumerate(books):
        if u['id']==user['id']:
            books[i] = user 
    return {}


app.run()
