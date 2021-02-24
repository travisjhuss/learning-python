from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def testfunction():
    return 'Testing a function on the same url'    

@app.route('/thatnewnew')
def thatnewnew():
    return 'Hey Im learning a new language!'