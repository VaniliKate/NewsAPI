from flask import Flask

from app.config import DevConfig
from .config import DevConfig

#App initialization
app = Flask(__name__,  template_folder='Templates', instance_relative_config = True)

#Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views