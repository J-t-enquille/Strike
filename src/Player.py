from Parser import Parser

class Player:
    def __init__(self, name, id=None):
        self.parser = Parser()
        self.name = name
        if self.parser.playerExist(name) != None:
            self.id = self.parser.playerExist(name)
        else:
            self.id = self.parser.lastIdPlayer() + 1

    def get_name(self):
        return self.name

