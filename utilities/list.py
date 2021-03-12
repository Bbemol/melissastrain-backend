class List:
    @staticmethod
    def filter(list: list, keys: list):
        return {key: list[key] for key in keys}
