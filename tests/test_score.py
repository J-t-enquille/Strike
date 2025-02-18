from src.Score import Score


def test_creation_score():
    score = Score()
    assert score is not None
    assert isinstance(score, Score)
    assert score.score == [None] * 10

    score2 = Score(5, 5)
    assert score2 is not None
    assert isinstance(score2, Score)
    assert score2.score == [None] * 5


def test_ajouterScore():
    score = Score()
    score.ajouterScore(0, 3, 4)
    score.ajouterScore(1, 7, 2)
    score.ajouterScore(7, 14, 7)
    assert score.score[0] == (3, 4)
    assert score.score[1] == (7, 2)
    assert score.score[7] is None
    assert score.ajouterScore(11, 1, 7) is False
    assert score.ajouterScore(7, 14, 7) is False

    score2 = Score(5, 5)
    score2.ajouterScore(0, 1, 3)
    assert score2.score[0] == (1, 3)
    assert score2.ajouterScore(6, 3, 1) is False
    assert score2.ajouterScore(2, 5, 4) is False


def test_affichage_score():
    score = Score()
    for i in range(10):
        score.ajouterScore(i)
        assert score.score[i] == (0, 0)


def test_affichage_score2(capsys):
    score = Score()
    score.ajouterScore(0, 3, 4)
    score.ajouterScore(1, 7, 2)
    score.ajouterScore(3, 5, 5)
    score.afficherLancer()

    captured = capsys.readouterr()
    expected_output = "\n--- Affichage des Lancer ---\nLancer n°1 = (3, 4)\nLancer n°2 = (7, 2)\nLancer n°4 = (5, 5)\n"
    assert captured.out == expected_output


def test_calculScoreLancer():
    score = Score(3)
    score.ajouterScore(0, 3, 4)
    score.ajouterScore(1, 8, 1)
    score.ajouterScore(2, 5, 5, 1)

    assert score.calculScoreLancer(0) == 7
    assert score.calculScoreLancer(1) == 9
    assert score.calculScoreLancer(2) == 11

    score2 = Score(3)
    score2.ajouterScore(0, 8, 2)
    score2.ajouterScore(1, 7, 2)
    score2.ajouterScore(2, 10, 10, 10)

    assert score2.calculScoreLancer(0) == 17
    assert score2.calculScoreLancer(1) == 9
    assert score2.calculScoreLancer(2) == 30

    score3 = Score(3)
    score3.ajouterScore(0, 10)
    score3.ajouterScore(1, 6, 1)
    score3.ajouterScore(2, 3, 5)

    assert score3.calculScoreLancer(0) == 17
    assert score3.calculScoreLancer(1) == 7
    assert score3.calculScoreLancer(2) == 8

    score4 = Score(3)
    score4.ajouterScore(0, 10)
    score4.ajouterScore(1, 10)
    score4.ajouterScore(2, 5, 3)

    assert score4.calculScoreLancer(0) == 25
    assert score4.calculScoreLancer(1) == 18
    assert score4.calculScoreLancer(2) == 8

    score5 = Score(3)
    score5.ajouterScore(0, 8, 2)
    score5.ajouterScore(1, 7, 3)
    score5.ajouterScore(2, 5, 5, 5)

    assert score5.calculScoreLancer(0) == 17
    assert score5.calculScoreLancer(1) == 15
    assert score5.calculScoreLancer(2) == 15

    score6 = Score(3)
    score6.ajouterScore(0, 8, 2)
    score6.ajouterScore(1, 10)
    score6.ajouterScore(2, 0, 8)

    assert score6.calculScoreLancer(0) == 20
    assert score6.calculScoreLancer(1) == 18
    assert score6.calculScoreLancer(2) == 8

    score7 = Score(3)
    score7.ajouterScore(0, 10)

    assert score7.calculScoreLancer(0) is None

    score8 = Score(3)
    score8.ajouterScore(0, 10)
    score8.ajouterScore(1, 10)
    score8.ajouterScore(2, 10, 10, 10)

    assert score8.calculScoreLancer(0) == 30
    assert score8.calculScoreLancer(1) == 30
    assert score8.calculScoreLancer(2) == 30


def test_score_total():
    score = Score()
    score.ajouterScore(0, 4, 5)
    score.ajouterScore(1, 2, 8)
    score.ajouterScore(2, 3, 0)
    scoreTotal = score.scoreTotal()

    assert scoreTotal == 25

    score2 = Score()
    score2.ajouterScore(0, 4, 5)
    score2.ajouterScore(1, 10)
    score2.ajouterScore(2, 3, 7)
    score2.ajouterScore(3, 4, 3)
    score_total2 = score2.scoreTotal()

    assert score_total2 == 50


def test_tableauScoreCourant():
    score = Score(5)
    score.ajouterScore(0, 8, 2)
    score.ajouterScore(1, 10)
    score.ajouterScore(2, 0, 8)
    score.ajouterScore(3, 10)
    score.ajouterScore(4, 5, 4)

    assert score.tableauScoreCourant() == [20, 38, 46, 65, 74]
    assert score.scoreTotal() == 74

    score2 = Score(3)
    score2.ajouterScore(0, 10)
    score2.ajouterScore(1, 10)
    score2.ajouterScore(2, 10, 10, 10)

    assert score2.tableauScoreCourant() == [30, 60, 90]

    score3 = Score(3)
    score3.ajouterScore(0, 10)

    assert score3.tableauScoreCourant() == []

    score4 = Score(3)
    score4.ajouterScore(0, 10)
    score4.ajouterScore(1, 3)

    assert score4.tableauScoreCourant() == [13, 16]


def test_calculScoreCourant():
    score = Score(5)
    score.ajouterScore(0, 8, 2)
    score.ajouterScore(1, 10)
    score.ajouterScore(2, 0, 8)
    score.ajouterScore(3, 10)
    score.ajouterScore(4, 5, 4)

    assert score.calculScoreCourant(0) == 20
    assert score.calculScoreCourant(1) == 38
    assert score.calculScoreCourant(2) == 46
    assert score.calculScoreCourant(3) == 65
    assert score.calculScoreCourant(4) == 74
    assert score.calculScoreCourant(5) is None

    score2 = Score(3)
    score2.ajouterScore(0, 10)
    score2.ajouterScore(1, 10)
    score2.ajouterScore(2, 10, 10, 10)

    assert score2.calculScoreCourant(0) == 30
    assert score2.calculScoreCourant(1) == 60
    assert score2.calculScoreCourant(2) == 90


def test_get_scores():
    score = Score()
    score.ajouterScore(0, 4, 5)
    score.ajouterScore(1, 2, 8)
    score.ajouterScore(2, 10)
    scores = score.getScores()

    assert scores == [(4, 5), (2, 8), (10, 0)]

    score2 = Score(3)
    score2.ajouterScore(0, 10)
    score2.ajouterScore(1, 10)
    score2.ajouterScore(2, 10, 10, 10)
    scores2 = score2.getScores()

    assert scores2 == [(10, 0), (10, 0), (10, 10, 10)]
