from utilities.list import List
from services.sncf import Endpoint, StationService
import json

class Station:
    @staticmethod
    def get(id: str):
        data = {"stationId": id}
        return Endpoint.make(data)

    @staticmethod
    def getArrivals(id: str):
        data = {"stationId": id, "arrivals": []}
        return Endpoint.make(data)

    # (!) The method below is legacy and needs to be reimplemented
    def LEGACY_getArrivalsData(stationId: str):
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
            # pass in the line types to filter the stations
            arrivals = StationService(id).get_arrivals_by_line_types([])
            result.append({"name": name, "id": id, "arrivals": arrivals})
        return json.dumps(result)
