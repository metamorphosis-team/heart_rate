# -*- coding: utf-8 -*-

from app import app

from fetch_heart_rate import get_heart_rate

@app.route('/')
def hello_world():
    heart_rate = get_heart_rate()
    return 'heart_rate:{}'.format(heart_rate)


if __name__ == '__main__':
    app.run()