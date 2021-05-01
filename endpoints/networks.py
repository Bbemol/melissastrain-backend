from services.sncf import Endpoint, LineTypesService

class Networks:
    @staticmethod
    def get():
        data = {"networks": id}
        Endpoint.make(data)

    #TODO: The method below is legacy and needs to be reimplemented
    @staticmethod
    def legacy_get_line_types():
        line_types = LineTypesService.get()
        return Endpoint.make(line_types)
