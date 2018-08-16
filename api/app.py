from flask import Flask
from routes import GetRoutes
app = Flask(__name__)
app.env = 'development'
app.testing = True 
GetRoutes.fetch_routes(app)

# @app.route('/')
# def hello_world():
#     return 'This is kalyango John api -inprogress'

if __name__ == '__main__':
    app.run(debug=True)