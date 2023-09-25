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

class SocialType(Enum):
    GLOBE = 1
    ENLIGHT = 2
    US_CIVIL = 3

class ELAType(Enum):
    R_AND_J = 0
    MACBETH = 1

class Card():
    def __init__(self,image = None,text : str = ""):
        if image != None:
            self.image_ref = Image.open(image)
            self.image_ref.resize((25,50))
            self.image = ImageTk.PhotoImage(self.image_ref)
        else:
            self.image = image
        self.text = text
        self.difficulty = 0

    def play(self):
        pass
    def refresh_image(self,image):
        if image != None:
            self.image_ref = Image.open(image)
            self.image_ref.resize((25,50))
            self.image = ImageTk.PhotoImage(self.image_ref)
        else:
            self.image = image

class SSCard(Card):
    def __init__(self,cardtype : SocialType):
        super().__init__(text="Social")
        self.type = cardtype
        self.difficulty = 1 #difficulty of the question
        self.question = "" #question asked
        self.options = [] #all possible options(4 total)
        self.answer = "" #Copy of correct answer, so that options can be scrambled, yes this can cause issues if they dont match... so hope that doesn't occur!
        match self.type:
            case SocialType.ENLIGHT:
                match randint(1,3):
                    case 1:
                        self.question = "Who wrote \"The Wealth of Nations\"?"
                        self.options.append("Adam Smith")
                        self.options.append("Voltaire")
                        self.options.append("Thomas Hobbes")
                        self.options.append("Jean Jaques Rousseau")
                    case 2:
                        self.question = "Who had the idea of the \"invisible hand\"?"
                        self.options.append("Adam Smith")
                        self.options.append("Voltaire")
                        self.options.append("Thomas Hobbes")
                        self.options.append("Jean Jaques Rousseau")
                    case 3:
                        self.question = "Who said, \"I may not agree with your opinions, but I will die fighting for your right to speak them.\"?"
                        self.options.append("Voltaire")
                        self.options.append("Adam Smith")
                        self.options.append("Mary Wollstonecraft")
                        self.options.append("Jean Jaques Rousseau")
                    
                    
        self.answer = self.options[0] #always put first option as correct, they are scambled anyway

    def play(self,window : Frame,rowsdown : int):
        shuffle(self.options)
        self.mc_question = mc.multiple_choice(self.options,self.options.index(self.answer),self.question,window,rowsdown=rowsdown)

class ELACard(Card): #Same as social, just placing it as a diff class for organization
    def __init__(self,cardtype : ELAType):
        super().__init__(text="ELA")
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
        super().__init__(text="Math")
        self.type = cardtype
        self.question = ""
        self.options = []
        self.answer = ""
        self.difficulty = 1
        #range/domain of the randints are completely arbitrary
        match self.type:
            case MathType.QUADRATICS:
                #base equation is either y = a(x-h)+k or y = ax^2 + bx + c
                self.refresh_image("include/Quadratics.png")
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
                                self.difficulty = 2
                                #get y intercept
                                self.question = f"What is the y-intercept of y = {a}((x{str_h})^2){str_k}?"
                                self.options.append(str(a*pow((-h),2)+k))
                                self.options.append(str(a*-(pow((k),2))+h))
                                self.options.append(str(a*-(pow((h),2))-k))
                                self.options.append(str(a*pow((k),2)-h))
                            case 2:
                                self.difficulty = 3
                                #x ints
                                self.question = f"What are the x-intercepts of y = {a}((x{str_h})^2){str_k}?"
                                self.options.append(f"{h}+/-{sqrt(abs((0-k)/a))}")
                                self.options.append(f"{k}+/-{sqrt(abs((0-h)/a))}")
                                self.options.append(f"{h}+/-{sqrt(abs((0-k)/-a))}")
                                self.options.append(f"{-h}+/-{sqrt(abs((0+k)/a))}")
                            case 3:
                                #vertex
                                self.question = f"What is the vertex of y = {a}((x{str_h})^2){str_k}?"
                                self.options.append(f"({-h},{k})")
                                self.options.append(f"({-k},{h})")
                                self.options.append(f"({h},{k})")
                                self.options.append(f"({k},{h})")
                    case 2:
                        #y = ax^2 + bx + c, I can only be bothered to do y int questions for this
                        a = randint(-10,10)
                        b = randint(-10,10)
                        c = randint(-25,25)
                        self.question = f"What is the y intercept of y = {a}x^2 + {b}x + {c}?"
                        self.options.append(f"{c}")
                        self.options.append(f"{-c}")
                        self.options.append(f"{a}")
                        self.options.append(f"{b}")
            case MathType.TRANSFORMATIONS:
                self.refresh_image("include\Transformations.png")
                #Find transformation in stretch, I can only be bothered to do stretch
                a = randint(-5,5)
                b = randint(-5,5)
                h = randint(-10,10)
                k = randint(-10,10)
                point_x = randint(-10,10)
                #Avoiding x/0:
                if point_x + h == 0:
                    h+=1
                if point_x - h == 0:
                    h+=1
                if point_x - k == 0:
                    k+=1
                if b == 0:
                    b+=1
                if a == 0:
                    a+=1
                point_y = randint(-10,10)
                self.difficulty = 2
                self.question = f"What is the vertical stretch of g({point_y}) = af({b}({point_x}-{h}))+{k} if f(x) = x?"
                self.options.append(f"{(point_y-k)/(b*(point_x-h))}")
                self.options.append(f"{(point_y-h)/(b*(point_x-k))}")
                self.options.append(f"{(point_y+k)/(b*(point_x+h))}")
                self.options.append(f"{(point_y-k)/(a*(point_x-h))}")
            case MathType.PERMS_AND_COMBS:
                self.refresh_image("include\Perms_And_Combs.png")
                #perm of a word, picking something, find perm k value, find comb k value
                n = randint(3,9)
                k = randint(3,n)
                match randint(1,4):
                    case 1: #find value of nPermk
                        self.question = f"How many different ways can you arrange {k} A's and {n-k} other unique letters?"
                        self.options.append(f"{perm(n,k)}")
                        self.options.append(f"{perm(k,n)}")
                        self.options.append(f"{perm(n+2,k)}")
                        self.options.append(f"{perm(n,k-1)}")
                    case 2: #find k value in nPermk
                        self.difficulty = 2
                        self.question = f"Find the k value of {n}!/k! = {perm(n,k)}"
                        self.options.append(f"{k}")
                        self.options.append(f"{n}")
                        self.options.append(f"{k+randint(1,2)}")
                        self.options.append(f"{k-randint(1,2)}")
                    case 3: #find value of nCombk
                        self.question = f"How many ways can you choose {k} letters from the first {n} letters of the alphabet"
                        self.options.append(f"{comb(n,k)}")
                        self.options.append(f"{comb(k,n)}")
                        self.options.append(f"{comb(n+2,k)}")
                        self.options.append(f"{comb(n,k-1)}")
                    case 4: #find k value in nCombk
                        self.difficulty = 2
                        self.question = f"Find the k value of {n}!/(({n}-k)!k!) = {comb(n,k)}"
                        self.options.append(f"{k}")
                        self.options.append(f"{n}")
                        self.options.append(f"{k+randint(1,2)}")
                        self.options.append(f"{k-randint(1,2)}")


        self.answer = self.options[0]

    def play(self,window : Frame,rowsdown : int):
        shuffle(self.options)
        self.mc_question = mc.multiple_choice(self.options,self.options.index(self.answer),self.question,master=window,rowsdown=rowsdown)