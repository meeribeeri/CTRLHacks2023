from random import randint
from random import random
from random import shuffle
import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *

from include.player import Player
from . import mc
from PIL import ImageTk, Image
from math import *

from enum import Enum

class MathType(Enum):
    QUADRATICS = 0
    TRANSFORMATIONS = 1
    PERMS_AND_COMBS = 2
    RADICALS_AND_EXPONENTS = 3

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
        if image != None:
            self.image_ref = Image.open(image)
            self.image_ref.resize((25,50),Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(self.image_ref)
        else:
            self.image = image
        self.text = text
        self.difficulty = 0

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
        self.question
        self.options = []
        self.answer = ""
        self.difficulty = 1
        match self.type:
            case MathType.QUADRATICS:
                #base equation is either y = a(x-h)+k or y = ax^2 + bx + c
                match randint(1,2):
                    case 1:
                        if randint(0,1) == 1:
                            a = randint(1,5)
                        else:
                            a = randint(1,5) * -1
                        h = randint(-30,30)
                        k = randint(-30,30)

                        if h >= 0:
                            str_h = f"-{h}"
                        else:
                            str_h = f"+{h*-1}"

                        if k >= 0:
                            str_k = f"+{k}"
                        else:
                            str_k = f"-{k*-1}"
                        match randint(1,3):
                            case 1:
                                #get y intercept
                                self.question = f"What is the y-intercept of y = {a}((x{str_h})^2){str_k}?"
                                self.options.append(str(a*pow((0-h),2)+k))
                                self.options.append(str(a*pow((0-k),2)+h))
                                self.options.append(str(a*pow((0+h),2)-k))
                                self.options.append(str(a*pow((0+k),2)-h))
                            case 2:
                                #x ints
                                self.question = f"What are the x-intercepts of y = {a}((x{str_h})^2){str_k}?"
                                self.options.append(f"+/-{sqrt(abs((0-k)/a))}+{h}")
                                self.options.append(f"+/-{sqrt(abs((0-h)/a))}+{k}")
                                self.options.append(f"+/-{sqrt(abs((0-k)/-a))}+{h}")
                                self.options.append(f"+/-{sqrt(abs((0+k)/a))}+{-h}")
                            case 3:
                                #vertex
                                self.question = f"What is the vertex of y = {a}((x{str_h})^2){str_k}?"
                                self.options.append(f"({-h},{k})")
                                self.options.append(f"({-k},{h})")
                                self.options.append(f"({h},{k})")
                                self.options.append(f"({k},{h})")

        self.answer = self.options[0]