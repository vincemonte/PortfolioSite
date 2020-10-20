from personalWebsite import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin): #inherin
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Project', backref='author', lazy=True)
    def __repr__(self):
        return f"User('{self.id}')"


#Parent
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    content= db.Column(db.Text, nullable=True)
    files = db.Column(db.String(80), nullable=True) #holds the path to the file images
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    home_post = db.relationship('HomePost', backref='project', uselist=False)
    def __repr__(self):
        return f"Post('{self.id}','{self.title}', '{self.date_posted}')"
#Child
class HomePost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), unique=True)
    type_image = db.Column(db.String(30), nullable=False)
    content = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return f"Post('{self.id}','{self.project_id}', '{self.type_image}')"
