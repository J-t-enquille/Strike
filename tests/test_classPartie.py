from src.Partie import Partie


def test_addPlayer():
    partie = Partie()
    partie.addPlayer("Maeva")
    assert "Maeva" in partie.scores


def test_addScore():
    partie = Partie()
    partie.addPlayer("Alice")
    partie.addScore("Alice", 0, 4, 5)
    assert partie.scores["Alice"].calculScoreCourant(0) == 9


def test_addScore_player_null():
    partie = Partie()
    result = partie.addScore("Bob", 0, 4, 5)
    assert result is False


def test_displayScores():
    nombretour = 10
    partie = Partie(["Alice", "Bob"])
    partie.addScore("Alice", 0, 4, 5)
    partie.addScore("Bob", 0, 10)

    scores = partie.displayScores()

    assert len(scores) == 2

    # Trouver le dictionnaire correspondant à Alice contenant son score
    # Premier dictionnaire de scores où le joueur est Alice
    alice_scores = next((item for item in scores if item["player"] == "Alice"), None)
    assert alice_scores is not None
    assert alice_scores["player"] == "Alice"
    assert alice_scores["total_score"] == 9
    assert alice_scores["tableau"] == [9] + [None] * (nombretour - 1)

    bob_scores = next((item for item in scores if item["player"] == "Bob"), None)
    assert bob_scores is not None
    assert bob_scores["player"] == "Bob"
    assert bob_scores["total_score"] == 10
    assert bob_scores["tableau"] == [None] * nombretour
