# -*- coding: utf-8 -*-
from app import app
import views
import models

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)