from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#setting the secret key
app.config['SECRET_KEY'] = '0612a219fbdcbb353bc09de164bee2ee'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#avoiding circular imports!
from personalWebsite import routes
