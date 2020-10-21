from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)


#setting the secret key
app.config['SECRET_KEY'] = '0612a219fbdcbb353bc09de164bee2ee'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#defining the upload folder path for easy file saving and loading
app.config['UPLOAD_FOLDER'] = os.path.join('images', 'project_images')
print(app.config['UPLOAD_FOLDER'])
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

#avoiding circular imports!
from personalWebsite import routes
