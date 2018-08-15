from flask import Flask
from urls import GetUrls
app = Flask(__name__)
app.env = 'development'
app.testing = True 
GetUrls.fetch_urls(app)

# @app.route('/')
# def hello_world():
#     return 'This is kalyango John api -inprogress'

if __name__ == '__main__':
    app.run(debug=True)