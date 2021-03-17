from services.sncf import Station, City
from utilities.list import List
from flask import Flask
import json

app = Flask(__name__)
@app.route('/')
def arrivals():
   return getArrivalsData()

def getArrivalsData():
    result = []

    paris_stations = City("Paris").get_stations()

    for station in paris_stations:
        name, id = List.filter(station, ["name", "id"]).values()
        arrivals = Station(id).get_arrivals()
        result.append({"name": name, "id": id, "arrivals": arrivals})
    return json.dumps(result)

def main():
    app.run()

if __name__ == '__main__':
    main()
