from card import Card
from typing import List
class TexasPlayer(object):
    def __init__(self,name,hand:List[Card]=None): # type: ignore
        self.name = name
        self.hand=[]

    def show(self):
        print("player" + self.name + ':',end=' ')
        for card in self.hand:
            card.show()