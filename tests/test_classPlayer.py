from src.Player import Player


def test_get_name(self):
    player = Player("Alice")
    assert player.get_name() == "Alice"

def test_id(self):
    player1 = Player("Alice")
    assert player1.get_id() == None
    player2 = Player("Alice", 1)
    assert player2.get_id() == 1
    #tester deux id soient differents