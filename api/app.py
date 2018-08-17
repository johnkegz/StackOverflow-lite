from flask import Flask
from routes import GetRoutes
App = Flask(__name__)
App.env = 'development'
App.testing = True 
GetRoutes.fetch_routes(App)
# @app.route('/')
# def hello_world():
#     return 'This is kalyango John api -inprogress'
if __name__ == '__main__':
    App.run(debug=True)