from src.Parser import Parser


def test_add_player():
    parser = Parser()
    parser.addPlayer("Test")
    assert parser.playerExist("Test") is not None
    assert parser.addPlayer("Test") is False


def test_lasted_id_player():
    parser = Parser()
    parser.addPlayer("Test")
    player = parser.getPlayers()[-1]
    assert parser.lastIdPlayer() == player.id


def test_delete_player():
    parser = Parser()
    parser.deleteAllPlayers()
    parser.addPlayer("Test")
    assert len(parser.getPlayers()) == 1
    assert parser.deletePlayer("Test") == True
    assert len(parser.getPlayers()) == 0
    assert parser.lastIdPlayer() == 0
    assert parser.playerExist("Test") is None


def test_delete_all_players():
    parser = Parser()
    parser.deleteAllPlayers()
    parser.addPlayer("Test")
    parser.addPlayer("Test2")
    assert len(parser.getPlayers()) == 2
    parser.deleteAllPlayers()
    assert len(parser.getPlayers()) == 0
