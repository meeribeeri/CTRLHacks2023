import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *
import include.card as cards
from include.menu import *
from include.player import Player
from include.mc import *
from include.misc import *
from PIL import ImageTk, Image
from math import *

def main():
    Win = Tk()

    Win.title('Card Learning Game') #self explanitory
    Win.geometry('1200x800') #Size of the window
    Win.resizable(False, False) #Window is not resizable
    Win.iconbitmap('') #Window Icon
    Win.grid_rowconfigure(0, weight=1)
    Win.grid_columnconfigure(0, weight=1)
    while True:
        

        winner = None
        
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
        
        Win.mainloop() #self explanitory
    #anything below here won't run, at least within the function
        if Player_1.hp <= 0:
            winner = 2
        else:
            winner = 1
        Player_1.delete()
        Player_2.delete()
        question_frame.delete()
        top_bar.delete()
        #deleting objs, probs unecessary
        del Player_1
        del Player_2
        del question_frame
        del top_bar

        end = EndScreen(master=Win,winner=winner)

        Win.mainloop()
        end.delete()
        del end
        

if __name__ == "__main__":
    main()
