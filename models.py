# -*- coding: utf-8 -*-
from app import db
import datetime


class HeartRate(db.Model):
    __tablename__ = 'heart_rate'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_time = db.Column(db.Time, default=datetime.datetime.now().time())
    user_id = db.Column(db.Integer, default=1)
    plan_id = db.Column(db.Integer, default=1)
    heart_rate = db.Column(db.Integer)

    def __init__(self, heart_rate):
        self.heart_rate = heart_rate

if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    heart_rate = HeartRate(80)
    db.session.add(heart_rate)
    db.session.commit()