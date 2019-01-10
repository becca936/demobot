from flask import  request
from demobot import app

@app.route('/weather')
def weather():

    temp = request.values.get('temp')
    temp = int(temp)

    if temp > 30:
        return "It's so hot!"
    else:
        return f"the temperature is {temp}"
