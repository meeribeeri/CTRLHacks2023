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
        self.x_resize = 50
        self.y_resize = 100
        if image != None:
            self.image_ref = Image.open(image)
            self.image_ref.resize((self.x_resize,self.y_resize))
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
            self.image_ref.resize((self.x_resize,self.y_resize))
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
                self.refresh_image("include\Enlightenment.png")
                all_people = ["Adam Smith","Voltaire","Thomas Hobbes","Mary Wollstonecraft","Jean Jacques Rousseau","John Locke","Baron Montesquieu"]
                match randint(1,8):
                    case 1:
                        self.question = "Who wrote \"The Wealth of Nations\"?"
                        self.options.append(all_people[0])
                    case 2:
                        self.question = "Who had the idea of the \"invisible hand\"?"
                        self.options.append(all_people[0])
                    case 3:
                        self.question = "Who said, \"I may not agree with your opinions, but I will die fighting for your right to speak them.\"?"
                        self.options.append(all_people[1])
                    case 4:
                        self.question = "Who thought that humans were born evil and needed society for order?"
                        self.options.append(all_people[2])
                    case 5:
                        self.question = 'Who believed that humans were born good and were corrupted by society?'
                        self.options.append(all_people[4])
                    case 6:
                        self.question = "Which enlightenment philosopher believed in gender equality the most?"
                        self.options.append(all_people[3])
                    case 7:
                        self.question = "Who believed that humans were born neutral, a blank slate to be filled?"
                        self.options.append(all_people[5])
                    case 8:
                        self.question = "Who presented the idea of the separation of powers in government?"
                        self.options.append(all_people[6])

                while len(self.options) < 4:
                    random_person = randint(0,6)
                    if self.options[0] == all_people[random_person]:
                        continue
                    else:
                        self.options.append(all_people[random_person])
            case SocialType.US_CIVIL:
                self.refresh_image("include\\US.png")
                match randint(1,4):
                    case 1:
                        self.question = "Which war started before the US Civil War?"
                        self.options.append("The Seven Years War/French and Indian War")
                        self.options.append("The Cold War")
                        self.options.append("WWI")
                        self.options.append("War of 1812")
                    case 2:
                        self.question = "What was the Tea Act of 1773 meant to combat?"
                        self.options.append("Smuggled Dutch tea")
                        self.options.append("Hostile colonists")
                        self.options.append("A boycott on British goods")
                        self.options.append("Minutemen")
                    case 3:
                        self.question = "Which battle did the \"Shot heard around the world\" fire?"
                        self.options.append("Lexington and Concord")
                        self.options.append("The Siege of Fort Ticonderoga")
                        self.options.append("Battle of Bunker Hill")
                        self.options.append("Battle of Trenton")
                    case 4:
                        self.question = "Who won the battle of New York City?"
                        self.options.append("Britain")
                        self.options.append("The colonists")
                        self.options.append("France")
                        self.options.append("Nobody")
            case SocialType.GLOBE:
                self.refresh_image("include\Globe.png")
                match randint(1,4):
                    case 1:
                        self.question = "Who suggested that more government intervention would help the economy?"
                        self.options.append("John Maynard Keynes")
                        self.options.append("Friedrick Hayek")
                        self.options.append("Milton Friedman")
                        self.options.append("Adam Smith")
                    case 2:
                        self.question = "What does CAVCO stand for?"
                        self.options.append("Canadian Audio Visual Certification Office")
                        self.options.append("Canadian Radio and Television Commission")
                        self.options.append("Canadian Broadcasting Corporation")
                        self.options.append("North America Free Trade Agreement")
                    case 3:
                        self.question = "Accommodation is:"
                        self.options.append("An inclusive approach allowing for distinct cultures")
                        self.options.append("Pushing a group to the \"margins\" of society")
                        self.options.append("The seperation of state and religion")
                        self.options.append("The integration of distinct minorities into society")
                    case 4:
                        self.question = "Acculturation is:"
                        self.options.append("Change to do contact with other cultures")
                        self.options.append("Reflecting many diverse cultures")
                        self.options.append("The growth of towns and cities")
                        self.options.append("The global popular culture from globalization")
                    
                    
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
                self.refresh_image("include\R_and_j.png")
                #total of 3 questions
                match randint(1,3):
                    case 1:
                        self.question = "Who says, \"A curse on both your houses!\"?"
                        self.options.append("Mercutio")
                        self.options.append("Tybalt")
                        self.options.append("Romeo")
                        self.options.append("Benvolio")
                    case 2:
                        self.question = "What event changed Lord Capulet & Montague?"
                        self.options.append("Romeo and Juliet's death")
                        self.options.append("Tybalt's death")
                        self.options.append("Romeo and Juliet's marriage")
                        self.options.append("Romeo's exile")
                    case 3:
                        self.question = "Why did Friar Laurence agree to marry Romeo and Juliet?"
                        self.options.append("To resolve the conflict between the two houses")
                        self.options.append("He owed Romeo a favour")
                        self.options.append("He liked Juliet")
                        self.options.append("He was bribed")
            case ELAType.MACBETH:
                self.refresh_image("include\Macbeth.png")
                #total of 4 options
                match randint(1,4):
                    case 1:
                        self.question = "The witches say that Macbeth shall be king and ____'s children as well."
                        self.options.append("Banquo")
                        self.options.append("Macbeth")
                        self.options.append("Siward")
                        self.options.append("Ross")
                    case 2:
                        self.question = "Who kills Macbeth?"
                        self.options.append("Macduff")
                        self.options.append("Malcolm")
                        self.options.append("Young Siward")
                        self.options.append("Himself")
                    case 3:
                        self.question = "Why does Macbeth kill Duncan?"
                        self.options.append("Ambition; to become the king")
                        self.options.append("To protect himself")
                        self.options.append("Hatred")
                        self.options.append("As a gift to his wife")
                    case 4:
                        self.question = "Why does Macbeth react strongly when he is told that the woods began to move?"
                        self.options.append("As he would never be killed until they moved")
                        self.options.append("As his enemies are attacking")
                        self.options.append("He thought they were removed")
                        self.options.append("He was drunk")
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
                self.question = f"What is the vertical stretch of g(x) = af({b}(x-{h}))+{k} if g({point_x}) = {point_y}?"
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