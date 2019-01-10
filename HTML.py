from flask import Flask, request
from demobot import app

@app.route('/ncss')
def hello_world():
    return "<h1>hello</h1>"


