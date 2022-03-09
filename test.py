from flask import Flask, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/pythonmongodb'
mongo = PyMongo(app)

@app.route('/users', methods=['POST'])
def create_user():
    print(request.json)
    return{'message': 'Received'}

if __name__ == '__main__':
    app.run(debug=True)