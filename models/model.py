"""
    File Name: model.py
    Create On: 2017/03/22
"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()
UBI_TABLE_PREFIX = "ubiwifi_"


class User(UserMixin, db.Model):
    """
    """
    __tablename__ = UBI_TABLE_PREFIX + "user"
    
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True)
    pass_word = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    join_date = db.Column(db.DateTime)
    is_activated = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return "<User {0}>".format(self.user_name)

    def verify_password(self, password):
        #return check_password_hash(self.pass_word, password)
        if self.pass_word == password:
            return True
        return False

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute.")

    @password.setter
    def password(self, password):
        self.pass_word = generate_password_hash(password)


class Device(db.Model):
    """
    """
    __tablename__ = UBI_TABLE_PREFIX + "device"
    
    user_id = db.Column(db.Integer, db.ForeignKey(UBI_TABLE_PREFIX+"user.id"))
    id = db.Column(db.Integer, primary_key=True)
    mac_address = db.Column(db.String(80), unique=True)
    manufacturer = db.Column(db.String(120))
    description = db.Column(db.String(1024))
    join_date = db.Column(db.DateTime)
    is_activated = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return "<Device {0}>".format(self.mac_address)

    def to_json(self):
        return {
            "id": self.id,
            "mac_address": self.mac_address,
            "manufacturer": self.manufacturer,
            "description": self.description,
            "join_date": self.join_date,
            "is_activated": self.is_activated
        }


class SSidConfig(db.Model):
    """
    """
    __tablename__ = UBI_TABLE_PREFIX + "ssidconifg"
    
    user_id = db.Column(db.Integer, db.ForeignKey(UBI_TABLE_PREFIX+"user.id"))
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    pass_word = db.Column(db.String(120))
    is_activated = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return "<SSidConfig {0}>".format(self.name)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "pass_word": self.pass_word,
            "is_activated": self.is_activated
        }


class UsageRecord(db.Model):
    """
    """
    __tablename__ = UBI_TABLE_PREFIX + "usagerecord"

    device_id = db.Column(db.Integer, db.ForeignKey(UBI_TABLE_PREFIX+"device.id"))
    id = db.Column(db.Integer, primary_key=True)
    data_usage = db.Column(db.Float)
    cost = db.Column(db.Boolean, default=True)
    begin_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    
    def __repr__(self):
        return "<UsageRecord {0}>".format(self.device_id)

    def to_json(self):
        return {
            "device_id": self.device_id,
            "id": self.id,
            "data_usage":self.data_usage,
            "begin_date": self.begin_date,
            "end_date": self.end_date
        }

