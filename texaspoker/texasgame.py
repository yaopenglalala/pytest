from poker import Poker
from card import Card
from card import getCardNum
from texasplayer import TexasPlayer
from typing import List

class TexasGame(object):
    #牌型定义
    cardShapeDict = {1:"Royal Flush",2:"Straight Flush",3:"Four of a Kind",4:"Full House",5:"Flush",6:"Straight",7:"Three of a Kind",8:"Two pairs",9:"Pair",10:"High card"}

    #最多发三轮牌
    maxRound = 3

    def __init__(self,playerNum=2,players:List[TexasPlayer]=None): # type: ignore
        self.poker = Poker()
        self.poker.removeJoker()
        self.poker.shuffle()

        if players == None:
            self.players = []
            for i in range(playerNum):
                self.players.append(TexasPlayer(str(i))) # type: ignore
        else :
            self.players = players
        
        self.desk = []

        self.round = 0

    #游戏前进一回合
    def deal(self):
        if self.round == 0:
             #第1回合要做的事情比较多
            for player in self.players:
                 player.hand.append(self.poker.popCard())
                 player.hand.append(self.poker.popCard())
            for i in range(3):
                self.desk.append(self.poker.popCard())        

        elif self.round < TexasGame.maxRound:
            self.desk.append(self.poker.popCard())
        
        else :
            print("No more round!")
            return
        
        self.round += 1 

        
    #展示桌面上的牌和玩家手里的牌,并给出当前最大牌型
    def showAll(self):
        print("Round" + str(self.round) + ":")

        #show desk
        self.showDesk()
        #show player
        for player in self.players:
            print("player" + player.name + ':',end=' ')
            for card in player.hand:
                card.show()
            maxCards = getMaxCardsFromOrigin(player.hand+self.desk)
            print(" —— " + TexasGame.cardShapeDict[seekShape(maxCards)[0]], end="")
            for card in maxCards:
                card.show()
            print()
    
    def showDesk(self):
        #show desk
        print("desk:", end=' ')
        for card in self.desk:
            card.show()
        print()


    #计算最终胜利的玩家
    def getWiner(self):
        drawMark = 0

        #初始化最大组合
        maxPlayer = []
        maxCards = [[]]

        for i in range(len(self.players)) : #逐个比较
            #获取玩家最大牌型
            challenger = self.players[i]
            challengerCards = getMaxCardsFromOrigin(self.desk[:] + challenger.hand)

            #最大牌型互相比较
            res = compareCardShape(maxCards[0],challengerCards)
            if res == 0:
                maxPlayer.append(challenger)
                maxCards.append(challengerCards)
                drawMark = 1
            elif res == 1:
                drawMark = 0
                continue
            elif res == 2:
                maxPlayer = [challenger]
                maxCards = [challengerCards]
                drawMark = 0
            else :
                print("bug?")

        print("Now winner:")
        for i in (maxPlayer):
            i.show()
        
        print("\nNow winner shape:")
        for i in (maxCards):
            for j in i:
                j.show()
        print("")
        return (maxPlayer,maxCards)

#获得多张牌中最大的五张牌牌型
def getMaxCardsFromOrigin(cards):
    maxCards = []

    #总共只有5张牌时，直接返回
    if (len(cards) == 5):
        maxCards = cards
    
    #6张牌中取5张对比大小=6张牌中去除1张比大小
    elif (len(cards) == 6):
        for i in range(6):
            challengerCards = cards[:]
            challengerCards.remove(cards[i])
            maxCards = getBiggerCards(maxCards,challengerCards)
    #7张牌中取5张对比大小=7张牌中去除2张比大小
    elif (len(cards) == 7):
        for i in range(6):
            for j in range(6-i):
                challengerCards = cards[:]
                challengerCards.remove(cards[i])
                challengerCards.remove(cards[i+j+1])
                maxCards = getBiggerCards(maxCards,challengerCards)
    return maxCards

#两牌型对比，返回一个更大的牌型(如果牌型相等则返回第一个牌型)
def getBiggerCards(list1, list2):
    res = compareCardShape(list1,list2)
    if res == 0:
        return list1
    elif res == 1:
        return list1
    elif res == 2:
        return list2
    else :
        print("bug?")

#比较两个德州牌型的大小，返回对比结论
def compareCardShape(list1, list2):
    if(len(list1) == 0):
        return 2

    if(len(list2) == 0):
        return 1

    if(len(list1) != 5):
        print("1error")
    
    if(len(list2) != 5):
        print("2error")

    res_1 = seekShape(list1)
    res_2 = seekShape(list2)
    if (res_1[0] < res_2[0]):
        return 1
    elif (res_1[0] > res_2[0]):
        return 2
    elif (res_1[0] == res_2[0]):
        for i in range(len(res_1)-1):
            if compareCardInList(res_1[i+1],res_2[i+1]) != 0:
                return compareCardInList(res_1[i+1],res_2[i+1])
    return 0

#牌型匹配
def seekShape(cards:List[Card]) -> List:
    if len(cards) != 5:
        print("Not texas!")
        return 0
    res = isRoyalFlush(cards)
    if (res[0] == 1):
        return 1,res[1]
    res = isStraightFlush(cards)
    if (res[0] == 1):
        return 2,res[1]
    res = isFour(cards)
    if (res[0] == 1):
        return 3,res[1],res[2]
    res = isFullHouse(cards)
    if (res[0] == 1):
        return 4,res[1],res[2]
    res = isFlush(cards)
    if (res[0] == 1):
        return 5,res[1]
    res = isStraight(cards)
    if (res[0] == 1):
        return 6,res[1]
    res = isThree(cards)
    if (res[0] == 1):
        return 7,res[1],res[2]
    res = isTwoPairs(cards)
    if(res[0] == 1):
        return 8,res[1],res[2],res[3]
    res = isPair(cards)
    if(res[0] == 1):
        return 9,res[1],res[2]
    res = isHighCard(cards)
    if(res[0] == 1):
        return 10,res[1]

#德州匹配规则
##皇家同花顺
def isRoyalFlush(cards:List[Card]):
    if (isStraightFlush(cards)[0] == 1 and cards[-1].number == 1):
        return 1,cards
    else : 
        return [0]

##同花顺
def isStraightFlush(cards:List[Card]):
    if (isStraight(cards)[0] and isFlush(cards)[0]):
        return 1,cards
    else :
        return [0]

##四条
def isFour(cards:List[Card]):
    cards = sortCards(cards)
    if (cards[0].number == cards[3].number):
        return 1,cards[:4], cards[4:]
    if (cards[1].number == cards[4].number):
        return 1,cards[1:5], cards[:1]
    return [0]

##葫芦
def isFullHouse(cards:List[Card]):
    a = isThree(cards)
    if a[0] == 1:
        two = a[2]
        if(isSameNum(two) == 1):
            return a
    return [0]

##同花
def isFlush(cards:List[Card]):
    if (isSameColor(cards) == 1):
        return 1,sortCards(cards)
    return [0]

##顺子
def isStraight(cards:List[Card]):
    cards = sortCards(cards,1)
    if (isStraightNum(cards)[0] == 1):
        return 1,cards
    return [0]

##三条
def isThree(cards:List[Card]):
    cards = sortCards(cards)
    if (cards[0].number == cards[2].number):
        return 1,cards[0:3], cards[3:]
    if (cards[1].number == cards[3].number):
        return 1,cards[1:4], [cards[0],cards[4]]
    if (cards[2].number == cards[4].number):
        return 1,cards[2:5],cards[0:2]
    return [0]

##两对
def isTwoPairs(cards:List[Card]):
    cards = sortCards(cards)
    maybepos = [0,2,4]
    for i in maybepos:
        tmp = cards.copy()
        tmp.remove(tmp[i])
        if(isSameNum(tmp[0:2]) and isSameNum(tmp[2:4])):
            return 1,tmp[2:4],tmp[0:2],[cards[i]]
    return [0]

##一对
def isPair(cards:List[Card]):
    cards = sortCards(cards)
    for i in range(len(cards) - 1):
        if(isSameNum([cards[i],cards[i+1]])):
            return 1,cards[i:i+2],cards[0:i]+cards[i+2:]
    return [0]

##高牌
def isHighCard(cards:List[Card]):
    return 1,sortCards(cards)


#数字基础规则
##数字是否相同
def isSameNum(cards:List[Card]):
    if(len(cards) == 1):
        return 0
    t_num = cards[0].number
    for card in cards:
        if card.number != t_num :
            return 0
    return 1

##是否连续，若是，返回连续的数组
def isStraightNum(cards:List[Card]):
    cardAmount = len(cards)
    if(cardAmount == 1):
        return [0]
    cards = sortCards(cards,1)

    #KA顺子特殊处理
    if (cards[0].number == 1) and (cards[cardAmount - 1].number == 13):
        t_num = 13
        for i in range(cardAmount - 2):
            if cards[cardAmount - 2 - i].number != t_num - 1:
                return [0]
            t_num = t_num -1
        cards.append(cards[0])
        cards.remove(cards[0])
        return 1,cards
    #常规顺子(含A2345型)
    t_num = cards[0].number
    for i in range(cardAmount - 1):
        if cards[i+1].number != t_num + 1:
            return [0]
        t_num = t_num + 1
    return 1,cards


#花色基础规则
##同花
def isSameColor(cards:List[Card]):
    if(len(cards) == 1):
        return 0
    t_color = cards[0].color
    for card in cards:
        if card.color != t_color :
            return 0
    return 1

#将牌按大小顺序排列
def sortCards(cards:List[Card],straightCase=0):
    cards.sort(key=getCardNum)
    if straightCase == 0:
        for i in range(len(cards)):
            if cards[0].number == 1:
                cards.append(cards[0])
                cards.remove(cards[0])
    return cards

#两张单牌比大小
def compareCard(card1:Card, card2:Card):
    if card1.number == card2.number :
        return 0
    elif card1.number == 1:
        return 1
    elif card2.number == 1:
        return 2
    elif card1.number > card2.number:
        return 1
    elif card1.number < card2.number:
        return 2
    else :
        print('error') 

#牌列表比单牌大小
def compareCardInList(card1:Card, card2:Card):
    # 长度不同不进行比较
    if len(card1) != len(card2) :
        print("list not same length")
        return

    card1 = sortCards(card1)
    card2 = sortCards(card2)
    for i in (range(len(card1)-1,-1,-1)):
        if compareCard(card1[i],card2[i]) != 0:
            return compareCard(card1[i],card2[i])
    return 0