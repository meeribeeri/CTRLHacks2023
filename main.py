import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *
import include.card as cards
from include.menu import TopBar
from include.player import Player
from include.mc import *
from include.misc import *



def main():
    Win = Tk()
    game_state = 0


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
    
    top_bar = TopBar(Win)

    question_frame = Question_Box(Win)

    deck = []
    for i in range(0,40):
        deck.append(cards.SSCard(cards.SocialType.ENLIGHT))
    Player_1 = Player(deck=deck,window=Win,question_area=question_frame)
    Player_2 = Player(deck=deck,window=Win,question_area=question_frame)
    question_frame.targets = [Player_1,Player_2]
    question_frame.retarget(1)
    Player_1.turnStart()
    
    print(game_state)
    Win.mainloop() #self explanitory
#anything below here won't run, at least within the function

if __name__ == "__main__":
    main()
