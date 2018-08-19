"""Module for starting/ running the app"""
from flask import Flask
from routes import GetRoutes
APP = Flask(__name__)
APP.env = 'development'
APP.testing = True
GetRoutes.fetch_routes(APP)
if __name__ == '__main__':
    APP.run(debug=True)
