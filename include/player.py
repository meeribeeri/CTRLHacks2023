from random import randint
import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *

class Player():
    def __init__(self,deck : list,hp : int = 100,max_hp : int = 100, window : Tk = None):
        self.hp = hp
        self.max_hp = max_hp
        self.deck = deck
        self.hand = []
        self.discard = []

        self.frame = Frame(master=window)
        self.frame.grid_rowconfigure(2, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.side_label = Label(master=self.frame,text="Cards:")
        self.side_label.grid(row=0,column=0,columnspan=2,sticky=N+S)

        self.frame_components = []

        while True:
            if len(self.hand) < 5:
                cardDrawn = deck.pop(randint(0,len(deck)-1))
                self.hand.append(cardDrawn)
            else:
                break

        for i in range(0,5):
            self.frame_components.append(Label(master=self.frame,text=self.hand[i].text,image=self.hand[i].image,compound=BOTTOM))
            self.frame_components[i*2].grid(row=1,column=i+1,sticky=N)
            self.frame_components.append(Label(master=self.frame,text=self.hand[i].text,image=self.hand[i].image,compound=BOTTOM))
            

    def damage(self, damage_taken : int):
        self.hp-=damage_taken

    def draw(self):
        for i in range(0,5-len(self.hand)):
            if len(self.deck) == 0:
                self.deck = self.discard
                self.discard = []
            cardDrawn = self.deck.pop(randint(0,len(self.deck)-1))
            self.hand.append(cardDrawn)
    def play(self,card_index,Win : Tk):
        card_used = self.hand.pop(card_index)
        self.discard.append(card_used)
        card_used.play(Win)

    def turnStart(self):
        for child in self.frame:
            child.configure(state='normal')
