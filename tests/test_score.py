from src.Score import Score

def test_creation_score():
    Score1 = Score()

def test_incrementation_score():
    Score2 = Score()
    Score2.ajouterScore(0,3,4)
    Score2.ajouterScore(1, 7, 2)
    Score2.ajouterScore(2, 1, 0)
    Score2.ajouterScore(11, 1, 7)
    Score2.ajouterScore(7, 14, 7)

def test_affichage_score():
    Score3 = Score()
    for i in range(10):
        Score3.ajouterScore(i)
    Score3.afficherLancer()

def test_calcul_lancer():
    Score4 = Score()
    Score4.ajouterScore(0, 3, 4)
    Score4.ajouterScore(1, 8, 1)
    Score4.ajouterScore(2, 8, 2)
    Score4.ajouterScore(3, 5, 2)
    Score4.ajouterScore(4, 10, 0)
    Score4.ajouterScore(5, 7, 2)
    print("")
    Score4.afficherLancer()
    assert(Score4.calculLancer(0) == 7)
    assert(Score4.calculLancer(1) == 9)
    assert(Score4.calculLancer(2) == 10)
    assert(Score4.calculLancer(3) == 12)
    assert(Score4.calculLancer(4) == 10)
    assert(Score4.calculLancer(5) == 18)

