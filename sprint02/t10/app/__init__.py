from flask import Flask
from app.controller import Controller
import os, config
from app.methods import Method
method = Method()

# создание экземпляра приложения

app = Flask(__name__)
control = Controller()


# import views
from . import views