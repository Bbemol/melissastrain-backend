from services.sncf import Endpoint

class Place:
    @staticmethod
    def get(id: str):
        data = {"placeId": id}
        return Endpoint.make(data)
