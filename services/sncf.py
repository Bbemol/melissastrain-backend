import requests
import re
from requests.models import HTTPBasicAuth
from utilities.env import Env
from utilities.list import List

SNCF_ENDPOINT = "https://api.sncf.com/v1/coverage/sncf/"

class SNCFService:
    token = Env.get("sncf-token")

    @staticmethod
    def get(path: str, params: set=None):
        url = SNCF_ENDPOINT + path
        response = requests.get(url, params=params, auth=HTTPBasicAuth(SNCFService.token, ''))
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

class City:
    def __init__(self, city: str):
        self.city = city

    @staticmethod
    def filter_stop_areas(place):
        return place["embedded_type"] == "stop_area"

    def get_stations(self):
        path = "/places"
        params = {"q": self.city}

        places = SNCFService.get(path, params)["places"]
        stop_areas = filter(City.filter_stop_areas, places)

        return list(stop_areas)
