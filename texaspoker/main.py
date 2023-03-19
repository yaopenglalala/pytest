import texasgame 
from texasgame import TexasGame
from card import Card

game = TexasGame(3)
#game.showAll()

game.deal()
game.showAll()
print('----')
game.getWiner()
print('---------')

game.deal()
game.showAll()
print('----')
game.getWiner()
print('---------')

game.deal()
game.showAll()
print('----')
game.getWiner()
print('---------')

# test = [Card(1,1),Card(2,9),Card(3,7),Card(4,3),Card(1,10),Card(4,3),Card(1,2)]
# maxCards = texasgame.getMaxCardsFromOrigin(test)
# print(":" + TexasGame.cardShapeDict[texasgame.seekShape(maxCards)[0]], end="")
# for card in maxCards:
#     card.show()
# print('---------')

# test1 = [Card(1,10),Card(2,11),Card(3,12),Card(4,13),Card(4,11)]
# print(TexasGame.cardShapeDict[texasgame.seekShape(test1)[0]])
# print(texasgame.compareCardShape(test,test1))
# print('---------')

# test2 = [Card(1,10),Card(1,11),Card(1,12),Card(1,13),Card(1,1)]
# print(TexasGame.cardShapeDict[texasgame.seekShape(test2)[0]])
# print(texasgame.compareCardShape(test1,test2))
# print('---------')

# game.deal()
# game.showNow()

# game.deal()
# game.showNow()

# print(game.getWiner())
