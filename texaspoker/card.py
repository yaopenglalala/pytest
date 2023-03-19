class Card(object):
    #1=方块 2=梅花 3=红桃 4=黑桃 5=鬼牌
    colorDict = {1:"♢",2:"♧",3:"♡",4:"♤",5:"鬼"}
    numDict = {1:"A",11:"J",12:"Q",13:"K",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10"}

    def __init__(self,color,number,isJoker=False):
        self.color = color
        self.number = number
        self.isJoker = isJoker

    def show(self):
        print('[' + str(Card.colorDict[self.color]) + " " + str(Card.numDict[self.number])  + ']', end = ' ')

def getCardNum(card:Card):
    return card.number