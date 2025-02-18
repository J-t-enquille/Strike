from src.Player import Player


def test_init_player():
    player = Player("Alice")
    assert player is not None
    assert isinstance(player, Player)


def test_get_name():
    player = Player("Alice")
    assert player.get_name() == "Alice"


def test_get_id():
    player1 = Player("Alice")
    assert player1.get_id() is None
    player2 = Player("Mathilde", 1)
    assert player2.get_id() == 1


def test_to_dict():
    player = Player("Alice", 1)
    assert player.to_dict() == {"name": "Alice", "id": 1}
    player2 = Player("Marie")
    assert player2.to_dict() == {"name": "Marie", "id": None}
