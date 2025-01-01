from flask import Flask
from flask_mysqldb import MySQL


mysql = MySQL()




def init_app(app):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'Nandu@1994'
    app.config['MYSQL_DB'] = 'dbname'
    mysql.init_app(app)
