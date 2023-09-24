from random import randint
from random import random
from random import shuffle
import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *

from include.player import Player
from . import mc

from enum import Enum

class MathType(Enum):
    OPERATOR = 0
    EXPONENT = 1
    VALUE = 2
    ABS = 3

class SocialType(Enum):
    GLOBE_U1 = 0
    GLOBE_U2 = 1
    GLOBE_U3 = 2
    GLOBE_U4 = 3
    ENLIGHT = 4
    US_CIVIL = 5

class ELAType(Enum):
    R_AND_J = 0
    MACBETH = 1

class Card():
    def __init__(self,image = None,text : str = ""):
        self.image = image
        self.text = text

    def play(self):
        pass

class SSCard(Card):
    def __init__(self,cardtype : SocialType):
        super().__init__(text="SS")
        self.type = cardtype
        self.difficulty = 1 #difficulty of the question
        self.question = "" #question asked
        self.options = [] #all possible options(4 total)
        self.answer = "" #Copy of correct answer, so that options can be scrambled, yes this can cause issues if they dont match... so hope that doesn't occur!
        match self.type:
            case SocialType.ENLIGHT:
                #temp only 1 option
                self.question = "Who wrote \"The Wealth of Nations\"?"
                self.options.append("Adam Smith")
                self.options.append("Voltaire")
                self.options.append("Thomas Hobbes")
                self.options.append("Jean Jaques Rousseau")
        self.answer = self.options[0] #always put first option as correct, they are scambled anyway

    def play(self,window : Frame,rowsdown : int):
        shuffle(self.options)
        self.mc_question = mc.multiple_choice(self.options,self.options.index(self.answer),self.question,window,rowsdown=rowsdown)

class ELACard(Card): #Same as social, just placing it as a diff class for organization
    def __init__(self,cardtype : ELAType):
        super.__init__(text="ELA")
        self.type = cardtype
        self.difficulty = 1 #difficulty of the question
        self.question = "" #question asked
        self.options = [] #all possible options(4 total)
        self.answer = "" #Copy of correct answer, so that options can be scrambled, yes this can cause issues if they dont match... so hope that doesn't occur!
        match self.type:
            case ELAType.R_AND_J:
                #temp only 1 option
                self.question = "Who says, \"A curse on both your houses!\"?"
                self.options.append("Mercutio")
                self.options.append("Tybalt")
                self.options.append("Romeo")
                self.options.append("Benvolio")
        self.answer = self.options[0]

    def play(self,window : Frame,rowsdown : int):
        shuffle(self.options)
        self.mc_question = mc.multiple_choice(self.options,self.options.index(self.answer),self.question,master=window,rowsdown=rowsdown)


class MathCard(Card):
    def __init__(self,cardtype : MathType):
        super.__init__(text="Math")
        self.type = cardtype
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
            case MathType.VALUE:
                self.value = "++"
                self.num = random()
                self.complexity+=1
            case MathType.ABS:
                self.value = "||"
                self.num = 0
                self.complexity = 1