#Coded by James
#This python code will run a coin toss to how many times you want it to flip.

import random
class Coin:
    def __init__(self):
        self._sideUp = "heads"
        self._numHeads = 0
        self._numTails = 0

    def toss(self):
        result = random.randint(0,1)
        if result==1:
            self._sideUp = "tails"
            self._numHeads+=1
        else:
            self._sideUp = "heads"
            self._numTails+=1
    
    def getSideUp(self):
        return self._sideUp

    def getNumHeads(self):
        return self._numHeads

    def getNumTails(self):
        return self._numTails