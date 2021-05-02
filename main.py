from endpoints.networks import NetworksEndpoint
from endpoints.place import PlaceEndpoint
from endpoints.station import StationEndpoint
from services.sncf import Endpoint
from flask import Flask
from flask_cors import CORS
from werkzeug.exceptions import Forbidden, InternalServerError, NotFound

app = Flask(__name__)
CORS(app)

@app.route('/')
def root():
    return '', 204

@app.route('/place/<geo_object>')
def get_place_by_geo_object(geo_object):
    return PlaceEndpoint().get(geo_object)

@app.route('/arrival/<arrivalId>')
def get_arrival_by_id(arrival_id):
    raise Forbidden()
    #TODO: return Arrival.get(arrival_id)

@app.route('/station/<station_id>')
def get_station_by_id(station_id):
    return StationEndpoint.get(station_id)

@app.route('/station/<station_id>/arrivals')
def get_arrivals_by_station_id(station_id):
    return StationEndpoint.get_arrivals(station_id)

@app.route('/station/<station_id>/networks')
def get_networks_by_station_id(station_id):
    return StationEndpoint.get_networks(station_id)

#TODO: Delete legacy endpoint
@app.route('/legacy/arrivals')
def legacy_get_arrivals_by_station_id():
    return StationEndpoint.legacy_get_arrivals_data()

#TODO: Delete legacy endpoint
@app.route('/legacy/networks')
def legacy_get_line_types():
    return NetworksEndpoint.get()

@app.errorhandler(InternalServerError)
def handle_500(e):
    return Endpoint.error(e)

@app.errorhandler(NotFound)
def handle_404(e):
     return Endpoint.error(e)

@app.errorhandler(Forbidden)
def handle_403(e):
     return Endpoint.error(e)

def main():
    app.run(debug=False)

if __name__ == '__main__':
    main()
