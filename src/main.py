from Parser import Parser


p = Parser()
p.addPlayer("Vladou")
p.addPlayer("Julie")
p.addPlayer("Gaston")
p.addPlayer("Gaston")
for play in p.getPlayers():
    print(play.name)

print(p.lastIdPlayer())
def assertTrue():
    return True
