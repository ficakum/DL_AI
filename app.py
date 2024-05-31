from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from databaseConnections.mongoConnection import *
from config import conf

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})  
api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    db = mongo_db_connect()
    app.run(host=conf["HOST"], port=int(conf["PORT"]))
