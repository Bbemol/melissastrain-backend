from endpoints.networks import Networks
from endpoints.arrival import Arrival
from endpoints.place import Place
from endpoints.station import Station
from services.sncf import Endpoint
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def root():
    return Endpoint.empty()

@app.route('/place/<placeId>')
def get_place_by_id(placeId):
    return Place.get(placeId)

@app.route('/arrival/<arrivalId>')
def get_arrival_by_id(arrivalId):
    return Arrival.get(arrivalId)

@app.route('/station/<stationId>')
def get_station_by_id(stationId):
    return Station.get(stationId)

@app.route('/station/<stationId>/arrivals')
def get_arrivals_by_station_id(stationId):
    return Station.get_arrivals(stationId)

#TODO: Delete legacy endpoint
@app.route('/station/legacy_arrivals')
def legacy_get_arrivals_by_station_id():
    return Station.legacy_get_arrivals_data()

#TODO: Delete legacy endpoint
@app.route('/station/legacy_networks')
def legacy_get_line_types():
    return Networks.legacy_get_line_types()

def main():
    app.run()

if __name__ == '__main__':
    main()
