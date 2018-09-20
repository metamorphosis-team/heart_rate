# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
app.secret_key = os.urandom(24)
app.config['DEBUG'] = True


