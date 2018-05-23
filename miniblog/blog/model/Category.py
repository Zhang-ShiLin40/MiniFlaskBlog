from blog import db1
from blog import *

class Category(db1.Model):
    __tablename__ = 'b_category'
    id = db1.Column(db1.Integer,primary_key=True)
    title = db1.Column(db1.String(20),unique=True)
    content = db1.Column(db1.String(100))

    def __init__(self,title,content):
        self.title = title
        self.content = content
    def __repr__(self):
        return '<Category %r>' % self.title