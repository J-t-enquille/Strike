class Score:
    def __init__(self):
        # Initialisation du tableau de tuples (int,int)
        # 1 tuple correspond à 1 lancé
        self.score = [None] * 10

    def ajouterScore(self, numeroLancer, lancer1, lancer2=0):
        if(0 <= numeroLancer < 10):
            self.score[numeroLancer] = (lancer1, lancer2)
        else:
            print("Numéro de lancer invalide")

    def afficherScore(self):
        print("Scores :")
        for i, score_tuple in enumerate(self.score):
            if score_tuple is not None:
                print(f"Lancer n°{i + 1} = {self.score[i]}")

    def calculLancer(self, numeroLancer):
        somme = self.score[numeroLancer][0] + self.score[numeroLancer][1]
        return somme

    def scoreTotal(self):
        sommeTotale = 0
        for i in range(10):
            sommeTotale = sommeTotale + self.calculLancer(i)
        return sommeTotale