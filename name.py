from flask import Flask, request
from demobot import app

@app.route('/greet', methods=['GET', 'POST'])
def greet_person():

    name = request.values.get('name')

    return f'hi {name}!'

