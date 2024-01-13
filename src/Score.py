class Score:
    def __init__(self):
        # Initialisation du tableau de tuples (int,int)
        # 1 tuple correspond à 1 lancé
        self.score = [None] * 10

    def ajouterScore(self, numeroLancer, lancer1=0, lancer2=0):
        if(0 <= numeroLancer < 10) & (lancer1 + lancer2 <= 10):
            self.score[numeroLancer] = (lancer1, lancer2)
        else:
            print(f"\nLancer invalide : n°{numeroLancer}, score {lancer1+lancer2}")

    def afficherLancer(self):
        print("\n--- Affichage des Lancer ---")
        for i, score_tuple in enumerate(self.score):
            if score_tuple is not None:
                print(f"Lancer n°{i + 1} = {self.score[i]}")

    def Spare(self, numeroLancer):
        if(self.score[numeroLancer][0] + self.score[numeroLancer][1] == 10):
            return True

    def Strike(self, numeroLancer):
        if(self.score[numeroLancer][0] == 10):
            return True

    def calculLancer(self, numeroLancer):
        if(numeroLancer == 0):
            somme = self.score[numeroLancer][0] + self.score[numeroLancer][1]
            return somme

        if(self.Strike(numeroLancer - 1)):
            somme = 2 * self.score[numeroLancer][0] + 2 * self.score[numeroLancer][1]
            return somme

        if(self.Spare(numeroLancer - 1)):
            somme = 2 * self.score[numeroLancer][0] + self.score[numeroLancer][1]
            return somme

        somme = self.score[numeroLancer][0] + self.score[numeroLancer][1]
        return somme

    def scoreTotal(self):
        sommeTotale = 0
        for i in range(10):
            sommeTotale = sommeTotale + self.calculLancer(i)
        return sommeTotale