from utilities.list import List
from services.sncf import Endpoint, SNCFService

class Networks:
    @staticmethod
    def get():
        data = {"networks": id}
        Endpoint.make(data)

    #TODO: The method below is legacy and needs to be reimplemented
    @staticmethod
    def legacy_get_networks():
        path = "networks"
        line_types = SNCFService.get(path, [], 86400)["networks"]
        line_types = List.filter_dict_list(line_types, ["id", "name"])
        return line_types

class NetworksEndpoint:
    @staticmethod
    def get():
        return Endpoint.make(Networks.legacy_get_networks())
