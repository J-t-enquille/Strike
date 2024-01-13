from Parser import Parser

class Player:
    def __init__(self, name, id=None):
        self.parser = Parser()
        self.name = name
        self.id = id

    def get_name(self):
        return self.name

    def to_dict(self):
        return {"name": self.name, "id": self.id}