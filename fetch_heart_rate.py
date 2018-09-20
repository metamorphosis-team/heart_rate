# -*- coding: utf-8 -*-

import requests
from app import db
from models import HeartRate
from time import sleep


class HeartRateFetcher:
    @classmethod
    def get_heart_rate(cls):
        r = requests.get('http://192.168.102.54:4035/gotapi/health/heartRate?accessToken=undefined&serviceId=F3%3A3B%3A15%3A7E%3A29%3ABB.a8e67eb5cd6341bef3872639e61514cc.localhost.deviceconnect.org')
        if r.status_code == 200:
            return r.json().get('heartRate')
        else:
            return -1


    @classmethod
    def add_heart_rate(cls):
        heart_rate = cls.get_heart_rate()
        if heart_rate != -1:
            db.session.add(HeartRate(heart_rate))
            db.session.commit()
            print("heart_rate_added:{}".format(heart_rate))

    # テストデータ取得用
    @classmethod
    def add_heart_rate_permanently(cls, interval_sec=1):
        for i in range(10000):
            cls.add_heart_rate()
            sleep(interval_sec)


if __name__ == '__main__':
    HeartRateFetcher.add_heart_rate_permanently()