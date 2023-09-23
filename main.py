import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *
import include.card as cards
from include.player import Player
from include.mc import *

def main():
    Win = Tk()

    Win.title('Card Learning Game') #self explanitory


    Win.geometry('1200x800') #Size of the window
    Win.resizable(False, False) #Window is not resizable
    Win.iconbitmap('') #Window Icon
    Win.grid_rowconfigure(0, weight=1)
    Win.grid_columnconfigure(0, weight=1)

    Ma=Menubutton(Win,text = 'Math') #This is the button for math!
    #add anything you need in here such as shape,geometry,mesh,etc
    #Ma.grid(column=0, row=0)#instead of using x,y coordinates i opted for colums and rows!
    def damage(damage : int):
        print(damage, "K")
    cardTest = cards.SSCard(damage,damage,cards.SocialType.ENLIGHT)
    cardTest.play(Win)

    """"
    Sci=Menubutton(Win,text = 'Science')
    Sci.grid(column=1, row=0)

    SoSt=Menubutton(Win,text = 'SS')
    SoSt.grid(column=2, row=0)

    Eng=Menubutton(Win,text = 'English')
    Eng.grid(column=3, row=0)


    Mul1 = Radiobutton(Win,text='34', value=1) #These are what we will use for multiple choice answers.
    Mul1.grid(column=0, row=3)

    Mul2 = Radiobutton(Win,text='65', value=2)
    Mul2.grid(column=1, row=3)

    Mul3 = Radiobutton(Win,text='87', value=3)
    Mul3.grid(column=2, row=3)"""



    def clicked():

        print #(.get())

    Butn = Radiobutton(Win, text="Click Me", command=clicked)
    #Butn.grid(column=3, row=3)

    SB = Spinbox(Win, from_=0, to=1000, width=10) # you can figure out h what this should do
    #SB.grid(column=0,row=5)

    Win.mainloop() #self explanitory


if __name__ == "__main__":
    main()
