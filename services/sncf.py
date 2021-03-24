import requests
import re
from utilities.env import Env
from utilities.list import List

SNCF_ENDPOINT = "https://api.sncf.com/v1/coverage/sncf/"

class SNCFService:
    token = Env.get("sncf-token")

    @staticmethod
    def get(path: str, params: set=None):
        url = SNCF_ENDPOINT + path
        response = requests.get(url, params=params, auth=(SNCFService.token, ''))
        status_code = response.status_code

        if status_code != 200:
            raise RuntimeError(f"Couldn't fetch the API. HTTP Code: {status_code}.")
        else:
            return response.json()

class Station:
    def __init__(self, station_id: str):
        self.station_id = Station.extract_id(station_id)

    @staticmethod
    def extract_id(station_id: str):
        regex = r"(.+:)(\d+)"
        print(f"{station_id} blabla")
        return re.search(regex, station_id).group(2)

    @staticmethod
    def create_query(station_id: int):
        return f"/stop_areas/stop_area:SNCF:{station_id}/arrivals"

    def get_arrivals(self):
        path = Station.create_query(self.station_id)
        arrivals = SNCFService.get(path)["arrivals"]

        filtered_arrivals = []

        for arrival in arrivals:
            filtered_arrivals.append(List.filter(arrival, ["display_informations", "stop_date_time"]))

        return filtered_arrivals

    def get_arrivals_by_line_types(self, line_types):
        # filter arrivals by line types
        return Station.get_arrivals(self)

class LineTypes:

    @staticmethod
    def get():
        path = "networks"
        line_types = SNCFService.get(path)["networks"]
        line_types = list(map(LineTypes.map_result, line_types))
        return line_types

    def map_result(line_type):
        mapped_line_infos = {}
        mapped_line_infos['name'], mapped_line_infos['id'] = List.filter(line_type, ["name", "id"]).values()
        return mapped_line_infos
