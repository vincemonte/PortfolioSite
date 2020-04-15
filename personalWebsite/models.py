from personalWebsite import db
from datetime import datetime

#Parent
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    content= db.Column(db.Text, nullable=True)
    images = db.Column(db.String(50), nullable=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
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
