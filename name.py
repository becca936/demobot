from flask import Flask, request

app = Flask(__name__)
@app.route('/greet', methods=['GET', 'POST'])
def greet_person():

    name = request.values.get('name')

    return f'hi {name}!'

app.run()