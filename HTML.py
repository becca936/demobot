from flask import Flask, request

app = Flask(__name__)

@app.route('/ncss')
def hello_world():
    return "<h1>hello</h1>"

if __name__ == '__main__':
    app.run()
