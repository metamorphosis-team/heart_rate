# -*- coding: utf-8 -*-

from app import app

from fetch_heart_rate import HeartRateFetcher
from flask import render_template

@app.route('/')
def hello_world():
    # heart_rate = HeartRateFetcher.get_heart_rate()
    # if heart_rate == -1:
    #     return "heart_rate_can't_fetch"
    return render_template('index.html')


if __name__ == '__main__':
    app.run()