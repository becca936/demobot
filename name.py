from flask import Flask, request


@app.route('/greet')
def greet_person():

    name = request.values.get('name')

    return f'hi {name}!'

app.run()