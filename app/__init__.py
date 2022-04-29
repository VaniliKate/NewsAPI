from flask import Flask

from app.config import DevConfig

#App initialization
app = Flask(__name__,  template_folder='Templates')

#Setting up configuration
app.config.from_object(DevConfig)

from app import views