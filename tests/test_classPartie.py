from src.Partie import Partie
from src.Player import Player

def test_addPlayer():
    partie = Partie()
    maeva=Player("Maeva")
    partie.addPlayer(maeva)
    assert maeva.get_name() in partie.scores


def test_addScore():
    partie = Partie()
    alice= Player("Alice")
    partie.addPlayer(alice)
    partie.addScore("Alice", 0, 4, 5)
    assert partie.scores["Alice"].calculScoreCourant(0) == 9

    assert partie.addScore("Lola", 0, 4, 5) is False

    partie2 = Partie([Player("Alice")], 10, 3)
    assert partie2.addScore("Alice", 0, 8, 5) is False


def test_addScore_player_null():
    partie = Partie()
    result = partie.addScore("Bob", 0, 4, 5)
    assert result is False


def test_displayScores():
    partie = Partie([Player("Alice"), Player("Bob"), Player("Lola")])
    partie.addScore("Alice", 0, 4, 5)
    partie.addScore("Alice", 1, 0, 0)
    partie.addScore("Alice", 2, 0, 0)
    partie.addScore("Bob", 0, 10)
    partie.addScore("Lola", 0, 8, 2)

    scores = partie.displayScores()

    assert len(scores) == 3

    # Trouver le dictionnaire correspondant à Alice contenant son score
    # Premier dictionnaire de scores où le joueur est Alice
    alice_scores = next((item for item in scores if item["player"] == "Alice"), None)
    assert alice_scores is not None
    assert alice_scores["player"] == "Alice"
    assert alice_scores["total_score"] == 9
    assert alice_scores["tableau"] == [9, 9, 9]

    bob_scores = next((item for item in scores if item["player"] == "Bob"), None)
    assert bob_scores is not None
    assert bob_scores["player"] == "Bob"
    assert bob_scores["total_score"] == 0
    assert bob_scores["tableau"] == []

    partie.addScore("Bob", 1, 4, 2)
    scores = partie.displayScores()
    bob_scores = next((item for item in scores if item["player"] == "Bob"), None)
    assert bob_scores["total_score"] == 22
    assert bob_scores["tableau"] == [16, 22]

    lola_scores = next((item for item in scores if item["player"] == "Lola"), None)
    assert lola_scores is not None
    assert lola_scores["player"] == "Lola"
    assert lola_scores["total_score"] == 0
    assert lola_scores["tableau"] == []

    partie.addScore("Lola", 1, 4, 2)
    scores = partie.displayScores()
    lola_scores = next((item for item in scores if item["player"] == "Lola"), None)
    assert lola_scores["total_score"] == 20
    assert lola_scores["tableau"] == [14, 20]

    partie2 = Partie([Player("Alice"), Player("Bob"), Player("Lola")], 5)
    partie2.addScore("Alice", 0, 8, 2)
    partie2.addScore("Alice", 1, 10)
    partie2.addScore("Alice", 2, 0, 8)
    partie2.addScore("Alice", 3, 10)
    partie2.addScore("Alice", 4, 5, 4)

    scores2 = partie2.displayScores()
    alice_scores2 = next((item for item in scores2 if item["player"] == "Alice"), None)

    assert alice_scores2["tableau"] == [20, 38, 46, 65, 74]
    assert alice_scores2["total_score"] == 74
    assert partie2.addScore("Alice", 5, 5, 4) is False

    partie3 = Partie([Player("Alice"), Player("Bob"), Player("Lola")], 10, 5)
    partie3.addScore("Alice", 0, 4, 1)
    partie3.addScore("Alice", 1, 5)
    partie3.addScore("Alice", 2, 0, 4)
    partie3.addScore("Alice", 3, 5)
    partie3.addScore("Alice", 4, 2, 2)

    scores3 = partie3.displayScores()
    alice_scores3 = next((item for item in scores3 if item["player"] == "Alice"), None)

    assert alice_scores3["tableau"] == [10, 19, 23, 32, 36]
    assert alice_scores3["total_score"] == 36
    assert partie3.addScore("Alice", 4, 4, 2) is False
    assert partie3.addScore("Alice", 11, 4, 2) is False
