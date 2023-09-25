import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *
import include.card as cards
from include.menu import *
from include.player import Player
from include.mc import *
from include.misc import *
from math import *
from random import randint
def main():
    Win = Tk()

    Win.title('Card Learning Game') #self explanitory
    Win.geometry('1000x500') #Size of the window
    Win.resizable(False, False) #Window is not resizable
    Win.iconbitmap('') #Window Icon
    Win.grid_rowconfigure(0, weight=1)
    Win.grid_columnconfigure(1, weight=1)
    while True:
        winner = None

        question_frame = Question_Box(Win)
        
        top_bar = TopBar(Win,question_frame)

        question_frame.get_topbar(topbar=top_bar)

        deck_p1 = []
        deck_p2 = []
        for i in range(0,20):
            card = None
            match randint(1,3):
                case 1:
                    #Math
                    card = cards.MathCard(cards.MathType(randint(0,2)))
                case 2:
                    #SS
                    card = cards.SSCard(cards.SocialType(randint(1,3)))
                case 3:
                    card = cards.ELACard(cards.ELAType(randint(0,1)))
            deck_p1.append(card)
        deck_p2 = deck_p1
        Player_1 = Player(deck=deck_p1,window=Win,question_area=question_frame,label_column=0,player_num=1)
        Player_2 = Player(deck=deck_p2,window=Win,question_area=question_frame,label_column=2,player_num=2)
        question_frame.targets = [Player_1,Player_2]

        question_frame.retarget(1)
        Player_1.turnStart()
        
        Win.mainloop() #self explanitory
    #anything below here won't run, at least within the function
        if Player_1.hp <= 0:
            winner = 2
            Player_2.side_frame.grid(row=1,column=0,sticky=N+E+W)
            Player_1.side_frame.destroy()
        else:
            winner = 1
            Player_1.side_frame.grid(row=1,column=0,sticky=N+E+W)
            Player_2.side_frame.destroy()

        Player_1.delete()
        Player_2.delete()
        question_frame.delete()
        top_bar.delete()

        end = EndScreen(master=Win,winner=winner)

        Win.mainloop()
        end.delete()
        if winner == 1:
            Player_1.side_frame.destroy()
        else:
            Player_2.side_frame.destroy()
        del end
        


main()
