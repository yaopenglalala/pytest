from card import Card
import random

class Poker(object):
    colorSet = [1,2,3,4,5] #1=方块 2=梅花 3=红桃 4=黑桃 5=鬼牌
    numberSet = range(1,13) #鬼牌的 1=小鬼；2=大鬼

    def __init__(self):
        self.cards = []
        for color in Poker.colorSet:
            if color != 5:
                for number in Poker.numberSet:
                    self.cards.append(Card(color,number))
        self.cards.append(Card(5,1,isJoker=True))
        self.cards.append(Card(5,2,isJoker=True))

    #移除大小鬼
    def removeJoker(self):
        for card in self.cards[:]:
            if card.isJoker == True:
                self.cards.remove(card)
    #洗牌
    def shuffle(self):
        random.shuffle(self.cards)
    
    #展示所有牌库里的牌
    def showCards(self):
        for card in self.cards:
            card.show
        print()

    #发一张牌
    def popCard(self):
        card = self.cards[0]
        self.cards.remove(card)
        return card