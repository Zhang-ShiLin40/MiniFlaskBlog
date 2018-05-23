#from blog import db1
from blog import *

class User(db1.Model):
    __tablename__ = 'b_user'
    id = db1.Column(db1.Integer,primary_key=True)
    username = db1.Column(db1.String(10),unique=True)
    password = db1.Column(db1.String(16))

    def __init__(self,username,password):
        self.username  = username
        self.password = password
    def __repr__(self):
        return '<User %r>' % self.username