from flask import Flask
from .config import DevConfig

#Intializing app
app = Flask(__name__)

#Setting configuration
 app.config.from_object(DevConfig) 

from app import views
