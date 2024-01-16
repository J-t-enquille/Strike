from src.Parser import Parser


def test_add_player():
    parser = Parser()
    parser.addPlayer("Test")
    assert parser.playerExist("Test") is not None


def test_lasted_id_player():
    parser = Parser()
    parser.addPlayer("Test")
    player = parser.getPlayers()[-1]
    assert parser.lastIdPlayer() == player.id


def test_delete_all_players():
    parser = Parser()
    parser.deleteAllPlayers()
    parser.addPlayer("Test")
    parser.addPlayer("Test2")
    assert len(parser.getPlayers()) == 2
    parser.deleteAllPlayers()
    assert len(parser.getPlayers()) == 0
