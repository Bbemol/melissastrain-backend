from services.sncf import Endpoint

class Arrival:
    @staticmethod
    def get(id: str):
        data = {"arrivalId": id}
        return Endpoint.make(data)
