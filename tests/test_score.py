from src.Score import Score
import pytest

def test_creation_score():
    Score1 = Score()
    assert Score1 is not None
    assert isinstance(Score1, Score)
    assert Score1.score == [None] * 10

    Score1_2 = Score(5, 5)
    assert Score1_2 is not None
    assert isinstance(Score1_2, Score)
    assert Score1_2.score == [None] * 5



def test_incrementation_score():
    Score2 = Score()
    Score2.ajouterScore(0,3,4)
    Score2.ajouterScore(1, 7, 2)
    Score2.ajouterScore(7, 14, 7)
    assert Score2.score[0] == (3,4)
    assert Score2.score[1] == (7,2)
    assert Score2.score[7] == None
    assert Score2.ajouterScore(11,1,7) == False
    assert Score2.ajouterScore(7, 14, 7) == False

    Score2_2 = Score(5,5)
    Score2_2.ajouterScore(0,1,3)
    assert Score2_2.score[0] == (1,3)
    assert Score2_2.ajouterScore(6,3,1) == False
    assert Score2_2.ajouterScore(2,5,4) == False



def test_affichage_score():
    Score3 = Score()
    for i in range(10):
        Score3.ajouterScore(i)
        assert Score3.score[i] == (0,0)
    #Score3.afficherLancer()



def test_affichage_score2(capsys):
    Score3 = Score()
    Score3.ajouterScore(0, 3, 4)
    Score3.ajouterScore(1, 7, 2)
    Score3.ajouterScore(3, 5, 5)
    Score3.afficherLancer()

    captured = capsys.readouterr()
    expected_output = "\n--- Affichage des Lancer ---\nLancer n°1 = (3, 4)\nLancer n°2 = (7, 2)\nLancer n°4 = (5, 5)\n"
    assert captured.out == expected_output



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
    assert Score4.calculLancer(0) == 7
    assert Score4.calculLancer(1) == 9
    assert Score4.calculLancer(2) == 10
    assert Score4.calculLancer(3) == 12
    assert Score4.calculLancer(4) == 10
    assert Score4.calculLancer(5) == 18
    assert Score4.calculLancer(6) == 0

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

def test_get_scores():
    score = Score()
    score.ajouterScore(0, 4, 5)
    score.ajouterScore(1, 2, 8)
    score.ajouterScore(2, 10)
    scores = score.getScores()

    assert scores == [(4, 5), (2, 8), (10, 0)]