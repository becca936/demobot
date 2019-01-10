from flask import Flask, request

app = Flask(__name__)

app.run()
@app.route('/weather')
def weather():

    temp = request.values.get('temp')
    temp = int(temp)

    if temp > 30:
        return "It's so hot!"
    else:
        return f"the temperature is {temp}"
