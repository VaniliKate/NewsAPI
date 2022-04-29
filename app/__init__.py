from flask import Flask

#App initialization
app = Flask(__name__,  template_folder='Templates')

from app import views