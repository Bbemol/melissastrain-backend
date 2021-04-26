class Dico:
    @staticmethod
    def map(dico: dict, function):
        return {key: function(value) for key, value in dico.items()}
