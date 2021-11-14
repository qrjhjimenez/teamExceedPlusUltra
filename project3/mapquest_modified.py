import urllib.parse
import requests
from flask import Flask
from flask import request
from flask import render_template

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "fZadaFOY22VIEEemZcBFfxl5vjSXIPpZ"

mapquest = Flask(__name__)

@mapquest.route("/", methods=['GET', 'POST'])
def input():
    global orig, dest, duration, distance, fuelused, metrica
    if request.method == "GET":
        return render_template('index.html')

    if request.method == "POST":
        orig = request.form['starting']
        dest = request.form['destination']
        metric = request.form['metrichtml']

        url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
        json_data = requests.get(url).json()

        if metric == "MILES":
            duration = (json_data["route"]["formattedTime"])
            distance = str(json_data["route"]["distance"]) + ' Miles'
            fuelused = str(json_data["route"]["fuelUsed"]) + ' Gal'
            metrica = 'FOR ' + metric

        elif metric == "KILOMETER":
            duration = (json_data["route"]["formattedTime"])
            distance = str("{:.2f}".format((json_data["route"]["distance"])*1.61)) + ' Kilometer'
            fuelused = str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)) + ' Ltr'
            metrica = 'FOR ' + metric

    return render_template('index.html', starting = orig, destination = dest, durahtml = duration, dishtml = distance,
        fuel = fuelused, metricb = metrica)

if __name__ == "__main__":
    mapquest.run(host="0.0.0.0", port=8080)