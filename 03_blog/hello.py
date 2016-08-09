from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

@app.route('/wfm')
def indexwfm():
 response = make_response('<h1>This document carries a cookie!</h1>')
 response.set_cookie('answer', '42')
 return response

@app.route('/user/<name>')
def user(name):
 return '<h1>Hello, %s!</h1>' % name
if __name__ == '__main__':
 app.run(debug=True)