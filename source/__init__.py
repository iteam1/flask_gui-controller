from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SERECT_KET'] = 'There is no serect key at all!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db =  SQLAlchemy(app)

from source import routes

