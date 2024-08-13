from flask import Flask
from routes.origins import origins
from flask_sqlalchemy import SQLAlchemy
from config import POSTGRESQL_CONNECTION_URI

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = POSTGRESQL_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

app.register_blueprint(origins)


