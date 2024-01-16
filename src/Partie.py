from src.Score import Score


class Partie:
    def __init__(self, players=None):
        self.scores = {}

        if players:
            for player in players:
                self.addPlayer(player)

    def addPlayer(self, player):
        if player not in self.scores:
            self.scores[player] = Score()

    def addScore(self, player, numeroLancer, lancer1=0, lancer2=0, lancer3=0):
        if player in self.scores:
            self.scores[player].ajouterScore(numeroLancer, lancer1, lancer2, lancer3)
        else:
            print(f"Le joueur {player} n'est pas dans la partie")
            return False

    def displayScores(self):
        result = []
        for player, score in self.scores.items():
            player_scores = {
                "player": player,
                "scores": score.getScores(),
                "tableau": score.tableauScore(),
                "total_score": score.scoreTotal()
            }
            result.append(player_scores)
        return result
