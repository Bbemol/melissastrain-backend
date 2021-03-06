import requests
from requests.models import HTTPBasicAuth
from utilities.env import Env

SNCF_ENDPOINT = "https://api.sncf.com/v1/coverage/sncf/"

class SNCFService:
    token = Env.get("sncf-token")

    @staticmethod
    def get(url):
        response = requests.get(url, auth=HTTPBasicAuth(SNCFService.token, ''))
        status_code = response.status_code

        if status_code != 200:
            raise RuntimeError(f"Couldn't fetch stop areas. HTTP Code: {status_code}.")
        else:
            return response.json()

class Station:
    def __init__(self, station_id):
        self.station_id = station_id

    @staticmethod
    def create_query(station_id):
        return f"/stop_areas/stop_area:SNCF:{station_id}/arrivals"

    def get_arrivals(self):
        url = SNCF_ENDPOINT + Station.create_query(self.station_id)

        return SNCFService.get(url)
