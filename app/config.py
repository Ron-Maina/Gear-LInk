from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_cors import CORS
import os


#app configuration
app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

#set a key for session management
app.secret_key = b'secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


db = SQLAlchemy()
#database initialization and migration
migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)