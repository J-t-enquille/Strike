import csv

path_file = "../src/data.csv"


class Parser:
    player = []

    def __init__(self, file_path=path_file):
        self.file_path = file_path

    def addPlayer(self, name):
        """
        Ajoute un joueur avec le nom donné au fichier CSV.
        Vérifie d'abord si le joueur existe déjà. Si non, ajoute le joueur,
        met à jour le fichier CSV et retourne True. Sinon, retourne False.
        """
        from src.Player import Player
        self.getPlayers()
        if self.playerExist(name) is None:
            self.player.append(Player(name, self.lastIdPlayer() + 1))
            with open(path_file, 'w') as file:
                fieldnames = ["name", "id"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for p in self.player:
                    writer.writerow(p.to_dict())
            return True
        return False

    def getPlayers(self):
        from src.Player import Player
        self.player = []
        with open(path_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                p = Player(row["name"], int(row["id"]))
                self.player.append(p)
        return self.player

    def playerExist(self, name):
        for p in self.player:
            if p.name == name:
                return p.id
        return None

    def lastIdPlayer(self):
        if len(self.player) > 0:
            return self.player[-1].id
        return 0

    def deleteAllPlayers(self):
        try:
            with open(self.file_path, 'w', newline='') as file:
                file.truncate(0)  # Remove all content from the file
                self.players = []  # Clear the players list
        except Exception as e:
            print(f"Error deleting all players: {e}")

    def deletePlayer(self, name):
        self.getPlayers()
        player_id = self.playerExist(name)
        if player_id is not None:
            self.player = [p for p in self.player if p.name != name]
            with open(path_file, 'w') as file:
                fieldnames = ["name", "id"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for p in self.player:
                    writer.writerow(p.to_dict())
            return True
        return False