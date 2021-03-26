class List:
    @staticmethod
    def filter(dico: dict, keys: list):
        return {key: dico[key] for key in keys}

    @staticmethod
    def filter_dico_list(list: list, keys: list):
        filteredList = []
        for item in list:
            filteredList.append(List.filter(item, keys))
        return filteredList

