from src.Score import Score


class Partie:
    def __init__(self, players=None, nombre_tours=10, nombre_quilles=10):
        self.scores = {}
        self.nombre_tours = nombre_tours
        self.nombre_quilles = nombre_quilles

        if players:
            for player in players:
                self.addPlayer(player)

    # Ajouter un joueur à la partie s'il n'est pas déjà présent
    def addPlayer(self, player):
        if player not in self.scores:
            self.scores[player] = Score(self.nombre_tours, self.nombre_quilles)

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
