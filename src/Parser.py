import json

path_file = "data.json"

class Parser:
    def addPlayer(self, player):
        with open(path_file, 'w') as file:
            obj = {
                "name": player.name,
                "id": player.id
            }
            json.dump(obj, file)

    def getPlayers(self):
        from Player import Player
        tableOfPlayer = []
        with open(path_file, 'r') as file:
            jsonData = json.load(file)
            for jsonObj in jsonData:
                tableOfPlayer.append(Player(jsonObj["name"] ,jsonObj["id"]));
        return tableOfPlayer

    def playerExist(self, name):
        for player in self.getPlayers():
            if player.name == name:
                return player.id
        return None

    def lastIdPlayer(self):
        return self.getPlayers()[-1].id
