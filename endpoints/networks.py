from os import stat
from services.sncf import Endpoint, LineTypes

import json

class Networks:
    @staticmethod
    def get():
        data = {"networks": id}
        Endpoint.make(data)

    # (!) The method below is legacy and needs to be reimplemented
    @staticmethod
    def line_types():
        line_types = LineTypes.get()
        return json.dumps(line_types)
