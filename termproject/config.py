import os
import pymysql

from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

SECRET_KEY = "MY_SECRET_KEY"

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'heartdisease'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)