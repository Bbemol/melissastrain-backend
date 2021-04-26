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
def getPlaceById(placeId):
    return Place.get(placeId)

@app.route('/arrival/<arrivalId>')
def getArrivalById(arrivalId):
    return Arrival.get(arrivalId)

@app.route('/station/<stationId>')
def getStationById(stationId):
    return Station.get(stationId)

@app.route('/station/<stationId>/arrivals')
def getArrivalsByStationId(stationId):
    return Station.getArrivals(stationId)

@app.route('/station/<stationId>/arrivals_legacy')
def getArrivalsByStationIdLegacy(stationId):
    return Station.LEGACY_getArrivalsData(stationId)

def main():
    app.run()

if __name__ == '__main__':
    main()
