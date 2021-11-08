from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from personalWebsite.config import DeployConfig

db = SQLAlchemy()
bcrypt = Bcrypt()


login_manager = LoginManager()
login_manager.login_view = 'main.home'
login_manager.login_message_category = 'info'

def create_app(config_class=DeployConfig):
    app = Flask(__name__)
    app.config.from_object(DeployConfig)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    #avoiding circular imports; we've now implented blueprints
    from personalWebsite.main.routes import main
    from personalWebsite.posts.routes import posts
    from personalWebsite.users.routes import users
    from personalWebsite.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(posts)
    app.register_blueprint(users)
    app.register_blueprint(errors)

    return app
