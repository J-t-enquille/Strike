from src.Score import Score
import pytest

def test_creation_score():
    Score1 = Score()

    assert(Score1 is not None)
    assert isinstance(Score1, Score)
    assert Score1.score == [None] * 10

def test_incrementation_score():
    Score2 = Score()
    Score2.ajouterScore(0,3,4)
    Score2.ajouterScore(1, 7, 2)
    print("")
    Score2.ajouterScore(7, 14, 7)

    assert Score2.score[0] == (3,4)
    assert Score2.score[1] == (7,2)
    assert Score2.score[7] == None

    assert Score2.ajouterScore(11,1,7) == False
    assert Score2.ajouterScore(7, 14, 7) == False


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

    # Tests asserts
    assert(Score4.calculLancer(0) == 7)
    assert(Score4.calculLancer(1) == 9)
    assert(Score4.calculLancer(2) == 10)
    assert(Score4.calculLancer(3) == 12)
    assert(Score4.calculLancer(4) == 10)
    assert(Score4.calculLancer(5) == 18)

def test_calcul_score():
    Score5 = Score()
    Score5.ajouterScore(0, 3, 4)
    Score5.ajouterScore(1, 8, 1)
    Score5.ajouterScore(2, 8, 2)
    Score5.ajouterScore(3, 5, 2)
    Score5.ajouterScore(4, 10, 0)
    Score5.ajouterScore(5, 7, 2)
    Score5.ajouterScore(6, 9, 1)
    Score5.ajouterScore(7, 10, 0)
    Score5.ajouterScore(8, 7, 0)
    Score5.ajouterScore(9,8,2,5)
    print("")
    Score5.afficherLancer()
    print("")
    Score5.affichageScoreCourant(9)

    assert(Score5.calculScoreCourant(2) == 26) #3 tours effectués
    assert(Score5.calculScoreCourant(4) == 48) #5 tours effectués
    assert(Score5.calculScoreCourant(7) == 96) #8 tours effectués
    assert(Score5.calculScoreCourant(9) == 125) #Tous les coups joués