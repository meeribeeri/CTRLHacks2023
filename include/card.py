from tkinter import ttk
from cardtypes import *
from random import randint
from random import random

class Card():
    def __init__(self):
        pass

    def use(self):
        pass

class MathCard(Card):
    def __init__(self,type : MathType):
        self.type = type
        self.value = ""
        self.num = 0
        self.complexity = 1
        match self.type:
            case MathType.OPERATOR:
                match randint(1,4):
                    case 1:
                        self.value = "+"
                        self.num = randint(1,50)
                    case 2:
                        self.value = "-"
                        self.num = randint(1,50)
                    case 3:
                        self.value = "*"
                        self.num = randint(2,10)
                        self.complexity+=1
                    case _:
                        self.value = "/"
                        self.num = randint(2,10)
                        self.complexity+=1
            case MathType.EXPONENT:
                self.value = "^"
                self.num = randint(2,4)
                self.complexity+=2