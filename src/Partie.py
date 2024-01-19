from src.Score import Score


class Partie:
    # passer un tableau d'objet Player en paramètre
    def __init__(self, players=None, nombre_tours=10, nombre_quilles=10):
        self.scores = {}
        self.nombre_tours = nombre_tours
        self.nombre_quilles = nombre_quilles

        if players is not None:
            for player in players:
                self.addPlayer(player)

    def setNombreTour(self, nombreTour):
        self.nombre_tours = nombreTour
        for player in self.scores:
            self.scores[player].setNombreTour(nombreTour)

    def setNombreQuille(self, nombreQuille):
        self.nombre_quilles = nombreQuille
        for player in self.scores:
            self.scores[player].setNombreQuille(nombreQuille)

    # Ajouter un joueur à la partie s'il n'est pas déjà présent
    # passer un objet Player en paramètre
    def addPlayer(self, player):
        if player.get_name() not in self.scores:
            self.scores[player.get_name()] = Score(self.nombre_tours, self.nombre_quilles)

    # Ajouter un score pour un joueur dans un tour spécifique
    def addScore(self, player, numerotour, lancer1=0, lancer2=0, lancer3=0):
        if player in self.scores:
            result = self.scores[player].ajouterScore(numerotour, lancer1, lancer2, lancer3)
            if result is False:
                return False
        else:
            print(f"Le joueur {player} n'est pas dans la partie")
            return False

    # Récupère les scores de tous les joueurs de la partie
    def displayScores(self):
        result = []
        for player, score in self.scores.items():
            player_scores = {
                "player": player,
                "scores": score.getScores(),
                "tableau": score.tableauScoreCourant(),
                "total_score": score.scoreTotal()
            }
            result.append(player_scores)
        return result
