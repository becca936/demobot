from flask import Flask, request
from demobot import app

@app.route('/ncss')
def hello():
    return "<h1>hello</h1>"


