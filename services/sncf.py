import requests
from requests.models import HTTPBasicAuth
from utilities.env import get_env

SNCF_ENDPOINT = "https://api.sncf.com/v1/coverage/sncf/"

def create_query(stop_area: int):
    return f"/stop_areas/stop_area:SNCF:{stop_area}/arrivals"

def get_stop_areas(id: int):
    token = get_env("sncf-token")
    url = SNCF_ENDPOINT + create_query(id)

    response = requests.get(url, auth=HTTPBasicAuth(token, ''))
    status_code = response.status_code

    if status_code != 200:
        raise RuntimeError(f"Couldn't fetch stop areas. HTTP Code: {status_code}.")
    else:
        return response.json()
