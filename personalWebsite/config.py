import os
class Config:
    #setting the secret key
    SECRET_KEY = '0612a219fbdcbb353bc09de164bee2ee'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    #defining the upload folder path for easy file saving and loading
    UPLOAD_FOLDER = os.path.join('images', 'project_images')
