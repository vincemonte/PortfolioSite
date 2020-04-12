from personalWebsite import db
from datetime import datetime
'''
class Post():
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    type_image = db.Column(db.String(20), nullable=False)
    content_synopsis = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=True)
    image = db.Column(db.String(20), nullable=True)
    date_posted = db.Column(db.DateTiime, nullable=False, default=datetime.utcnow)
    def __repr__(self):
        return f"Post('{self.id}','{self.title}', '{self.date_posted}')"
'''

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    type_image = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text, nullable=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    def __repr__(self):
        return f"Post('{self.id}','{self.title}', '{self.date_posted}', '{self.type_image}')"
