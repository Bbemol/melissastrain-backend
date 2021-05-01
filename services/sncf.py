from flask.helpers import make_response
import requests
import requests_cache
import re
import json
from utilities.env import Env
from utilities.list import List

SNCF_ENDPOINT = "https://api.sncf.com/v1/coverage/sncf/"

class SNCFService:
    token = Env.get("sncf-token")

    @staticmethod
    def get(path: str, params: set=None, ttl: int=180):
        if ttl != 0:
            requests_cache.install_cache('sncf_cache', backend='sqlite', expire_after=ttl)
        url = SNCF_ENDPOINT + path
        response = requests.get(url, params=params, auth=(SNCFService.token, ''))
        status_code = response.status_code

        if status_code != 200:
            raise RuntimeError(f"Couldn't fetch the API. HTTP Code: {status_code}.")
        else:
            return response.json()

class Endpoint:
    @staticmethod
    def make(data, mimetype='application/json'):
        data = json.dumps(data)
        response = make_response(data)
        response.mimetype = mimetype
        return response

    @staticmethod
    def not_implemented():
        return Endpoint.make({"error": "Not yet implemented"})

    @staticmethod
    def empty():
        return Endpoint.make({"error": "Empty response"})

class StationService:
    def __init__(self, station_id: str):
        self.station_id = StationService.extract_id(station_id)

    @staticmethod
    def extract_id(station_id: str):
        regex = r"(.+:)(\d+)"
        return re.search(regex, station_id).group(2)

    @staticmethod
    def create_query(station_id: int):
        return f"/stop_areas/stop_area:SNCF:{station_id}/arrivals"

    def get_arrivals(self):
        path = StationService.create_query(self.station_id)
        arrivals = SNCFService.get(path)["arrivals"]
        filtered_arrivals = List.filter_dico_list(arrivals, ["display_informations", "stop_date_time"])
        return filtered_arrivals

    def get_arrivals_by_line_types(self, line_types):
        # filter arrivals by line types
        all_arrivals = StationService.get_arrivals(self)
        filtered_arrivals = all_arrivals
        return filtered_arrivals

class LineTypesService:

    @staticmethod
    def get():
        path = "networks"
        line_types = SNCFService.get(path)["networks"]
        line_types = List.filter_dico_list(line_types, ["id", "name"])
        return line_types
