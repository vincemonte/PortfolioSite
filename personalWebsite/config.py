import json
import os

with open('/etc/config.json') as config_file:
	config = json.load(config_file)

class DeployConfig:
    #setting the secret key
	SECRET_KEY = config.get('SECRET_KEY')
	SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
    #defining the upload folder path for easy file saving and loading
	UPLOAD_FOLDER = os.path.join('images', 'project_images')
