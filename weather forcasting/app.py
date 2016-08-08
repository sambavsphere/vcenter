from flask import Flask,render_template,request
app = Flask(__name__)
import pyowm
import pdb
import json
def get_weather(city):
    owm = pyowm.OWM('cfb6b9a4f8e09ec97f2959058f490a4d')  
    forecast = owm.daily_forecast(city)
    w1=forecast.get_forecast()
    weathers = w1.get_weathers()[:5]
    result = []
    for i in weathers:
        result.append(i.to_JSON())
    return json.dumps(result)

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    city='London,uk'
    weathers = get_weather(city)
    if request.method == 'POST':
        city = request.form['city']
        if city:
            weathers = get_weather(city)
            return render_template('home.html', city=city,weathers=weathers)
    return render_template('home.html', city=city,weathers=weathers)
app.run(port=8080)