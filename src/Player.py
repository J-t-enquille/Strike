from Parse import Parse
class Player:
    def __init__(self, name, id=None):
        self.parser = Parse()
        self.name = name
        """verifier si le joueur existe deja avec fonction parser et si oui, on recupere son id"""
        self.id = id

    def get_name(self):
        return self.name