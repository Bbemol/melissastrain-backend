from services.sncf import Endpoint, SNCFService

class Place:
    def __init__(self, geo_object: str):
        self.geo_object = geo_object

    @staticmethod
    def create_query(geo_object: str, type: str="stop_point"):
        return f"/places?q={geo_object}&type[]={type}"

    def get(self):
        path = Place.create_query(self.geo_object)
        station = SNCFService.get(path, [], 86400)
        return station

class PlaceEndpoint:
    @staticmethod
    def get(geo_object: str):
        return Endpoint.make(Place(geo_object).get())
