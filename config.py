# -*- coding: utf-8 -*-
import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///heart_rate.db'
SECRET_KEY = os.urandom(24)
SQLALCHEMY_TRACK_MODIFICATIONS = True