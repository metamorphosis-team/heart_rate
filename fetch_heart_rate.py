# -*- coding: utf-8 -*-


from pprint import pprint
import requests
from requests.auth import HTTPBasicAuth

def get_heart_rate():
    r = requests.get('http://192.168.102.54:4035/gotapi/health/heartRate?accessToken=undefined&serviceId=F3%3A3B%3A15%3A7E%3A29%3ABB.a8e67eb5cd6341bef3872639e61514cc.localhost.deviceconnect.org')
    if r.status_code == 200:
        return r.json().get('heartRate')
    else:
        return -1


if __name__ == '__main__':
    get_heart_rate()