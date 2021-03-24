from services.sncf import Station
from utilities.list import List
from flask import Flask
import json

app = Flask(__name__)
@app.route('/')
def arrivals():
   return getArrivalsData()

def getArrivalsData():
    result = []

    paris_stations = [
        {'id': 'stop_area:SNCF:87384008', 'name': 'Saint-Lazare'},
        {'id': 'stop_area:SNCF:87686006', 'name': 'Gare de Lyon'},
        {'id': 'stop_area:SNCF:87391003', 'name': 'Montparnasse'},
        {'id': 'stop_area:SNCF:87271007', 'name': 'Paris Nord'},
        {'id': 'stop_area:SNCF:87547000', 'name': 'Paris Austerlitz'}
    ]

    for station in paris_stations:
        name, id = List.filter(station, ["name", "id"]).values()
        arrivals = Station(id).get_arrivals()
        result.append({"name": name, "id": id, "arrivals": arrivals})
    return json.dumps(result)

def main():
    app.run()

if __name__ == '__main__':
    main()
