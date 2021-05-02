from utilities.list import List
from services.sncf import Endpoint, SNCFService
import re

class Station:
    def __init__(self, station_id: str):
        self.station_id = Station.extract_id(station_id)

    @staticmethod
    def extract_id(station_id: str):
        regex = r"(.+:)(\d+)"
        return re.search(regex, station_id).group(2)

    @staticmethod
    def create_query(station_id: int, type: str=""):
        return f"/stop_areas/stop_area:SNCF:{station_id}/{type}"

    def get(self):
        return {"station_id": self.station_id}

    def get_arrivals(self):
        path = Station.create_query(self.station_id, "arrivals")
        arrivals = SNCFService.get(path)["arrivals"]
        filtered_arrivals = List.filter_dict_list(arrivals, ["display_informations", "stop_date_time"])
        return filtered_arrivals

    def get_networks(self):
        path = Station.create_query(self.station_id, "networks")
        networks = SNCFService.get(path)["networks"]
        return networks

    #TODO: The method below is legacy and needs to be reimplemented
    def legacy_get_arrivals_data():
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
            arrivals = Station(id).get_arrivals()
            result.append({"name": name, "id": id, "arrivals": arrivals})
        return result

class StationEndpoint:
    @staticmethod
    def get(station_id: str):
        return Endpoint.make(Station(station_id).get())

    @staticmethod
    def get_arrivals(station_id: str):
        return Endpoint.make(Station(station_id).get_arrivals())

    @staticmethod
    def get_networks(station_id: str):
        return Endpoint.make(Station(station_id).get_networks())

    @staticmethod
    def legacy_get_arrivals_data():
        return Endpoint.make(Station.legacy_get_arrivals_data())
