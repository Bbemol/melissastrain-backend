from flask.helpers import make_response
import requests
import requests_cache
import json
from utilities.env import Env

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
    def error(e):
        response = e.get_response()
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description
        })
        response.mimetype = 'application/json'
        return response
