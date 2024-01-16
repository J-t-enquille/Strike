class Score:
    def __init__(self, nombreTour=10, nombreQuille=10):
        # Initialisation du tableau de tuples (int,int)
        # 1 tuple correspond à 1 lancé
        self.nombreTour = nombreTour
        self.nombreQuille = nombreQuille
        self.score = [None] * nombreTour

    def ajouterScore(self, numeroLancer, lancer1=0, lancer2=0, lancer3=0):
        if 0 <= numeroLancer < self.nombreTour - 1:
            if lancer1 + lancer2 <= self.nombreQuille:
                self.score[numeroLancer] = (lancer1, lancer2)
            else:
                # print(f"Lancer invalide : n°{numeroLancer}, score {lancer1+lancer2}")
                return False
        elif numeroLancer == self.nombreTour - 1:
            if lancer1 == self.nombreQuille or lancer1 + lancer2 == self.nombreQuille:  # Strike ou Spare
                self.score[numeroLancer] = (lancer1, lancer2, lancer3)
            else:
                self.score[numeroLancer] = (lancer1, lancer2)
        else:
            # print(f"Lancer invalide : n°{numeroLancer}")
            return False


    def afficherLancer(self):
        print("\n--- Affichage des Lancer ---")
        for i, score_tuple in enumerate(self.score):
            if score_tuple is not None:
                print(f"Lancer n°{i + 1} = {self.score[i]}")

    def Spare(self, numeroLancer):
        if self.score[numeroLancer][0] + self.score[numeroLancer][1] == self.nombreQuille:
            return True

    def Strike(self, numeroLancer):
        if self.score[numeroLancer][0] == self.nombreQuille:
            return True

    def calculLancer(self, numeroLancer):
        if self.score[numeroLancer] is None:
            return 0
        if numeroLancer == 0:
            somme = self.score[numeroLancer][0] + self.score[numeroLancer][1]
            return somme

        if self.Strike(numeroLancer - 1):
            somme = 2 * self.score[numeroLancer][0] + 2 * self.score[numeroLancer][1]
            return somme

        if self.Spare(numeroLancer - 1):
            somme = 2 * self.score[numeroLancer][0] + self.score[numeroLancer][1]
            return somme

        if numeroLancer == self.nombreTour - 1:
            if (self.score[numeroLancer][0] == self.nombreQuille
                    or self.score[numeroLancer][0] + self.score[numeroLancer][1] == self.nombreQuille):
                somme = self.score[numeroLancer][0] + self.score[numeroLancer][1] + self.score[numeroLancer][2]
                return somme

        somme = self.score[numeroLancer][0] + self.score[numeroLancer][1]
        return somme

    def calculScoreCourant(self, numeroLancer):
        scoreCourant = 0
        for i in range(0, numeroLancer+1):
            scoreCourant = scoreCourant + self.calculLancer(i)
            # print(f"Score après lancer n°{i + 1} = ", scoreCourant)
        return scoreCourant

    def affichageScoreCourant(self, numeroLancer):
        scoreCourant = 0
        for i in range(0, numeroLancer + 1):
            scoreCourant = scoreCourant + self.calculLancer(i)
            print(f"Score après lancer n°{i + 1} = ", scoreCourant)

    def scoreTotal(self):
        sommeTotale = 0
        for i in range(10):
            sommeTotale = sommeTotale + self.calculLancer(i)
        return sommeTotale

    def getScores(self):
        return [score_tuple for score_tuple in self.score if score_tuple is not None]