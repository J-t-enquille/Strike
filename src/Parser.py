import json

path_file = "data.json"

class Parser:
    def addPlayer(self, name):
        with open(path_file, 'w') as file:
            json.dump(name, file)

    def getPlayer(self):
        tableOfPlayer = []
        with open(path_file, 'r') as file:
            jsonData = json.load(file)
            for jsonObj in jsonData:
                Player(jsonObj[id])
                tableOfPlayer.append()

