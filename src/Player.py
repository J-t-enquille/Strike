from src.Parser import Parser


class Player:
    def __init__(self, name, idP=None):
        self.parser = Parser()
        self.name = name
        self.id = idP

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    # Convertir un objet joueur en un dictionnaire
    def to_dict(self):
        return {"name": self.name, "id": self.id}
