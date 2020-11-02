import os
class Config:
    #setting the secret key
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    #defining the upload folder path for easy file saving and loading
    UPLOAD_FOLDER = os.path.join('images', 'project_images')
