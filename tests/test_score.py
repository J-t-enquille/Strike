from src.Score import Score

def test_creation_score():
    Score1 = Score()

def test_incrementation_score():
    Score2 = Score()
    Score2.ajouterScore(0,3,4)
    Score2.ajouterScore(1, 7, 2)
    Score2.ajouterScore(2, 1, 0)

def test_affichage_score():
    Score3 = Score()
    Score3.ajouterScore(0, 3, 4)
    Score3.ajouterScore(1, 0, 0)
    Score3.afficherScore()

def test_calcul_lancer():
    Score4 = Score()
    Score4.ajouterScore(0, 3, 4)
    Score4.calculLancer(0)
    assert(Score4.calculLancer(0) == 7)

