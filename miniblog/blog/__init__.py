# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


#加载配置文件内容
app.config.from_object('blog.setting')     #模块下的setting文件名，不用加py后缀
app.config.from_envvar('FLASKR_SETTINGS')   #环境变量，指向配置文件setting的路径
from flask_sqlalchemy import SQLAlchemy


#创建数据库对象
db1 = SQLAlchemy(app)

from blog.controller import blog_message
from blog.model import Category, User#需注意引入包的顺序，避免循环调用
