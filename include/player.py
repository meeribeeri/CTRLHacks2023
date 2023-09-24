from random import randint
import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *


class Player():
    def __init__(self,question_area,deck : list, window : Tk = None):
        self.deck = deck
        self.hand = []
        self.discard = []
        self.question_area = question_area
        #
        self.cards_to_play = [BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar()]
        self.master = window

        self.frame = Frame(master=window)
        self.frame['borderwidth'] = 2
        self.frame['relief'] = 'sunken'
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
            self.frame_components.append(Checkbutton(master=self.frame,text="Play",onvalue=True,offvalue=False,variable=self.cards_to_play[i]))
            self.frame_components[i*2+1].grid(row=2,column=i+1,sticky=N)
        self.frame_components.append(Button(master=self.frame,text="Play Cards",command=self.endCardChoice))
        self.frame_components[10].grid(row=3,column=0,columnspan=6,sticky=N)
            

    def draw(self):
        for i in range(0,5-len(self.hand)):
            if len(self.deck) == 0:
                self.deck = self.discard
                self.discard = []
            cardDrawn = self.deck.pop(randint(0,len(self.deck)-1))
            self.hand.append(cardDrawn)

    def play(self,card_index,rowsdown : int):
        try:
            card_used = self.hand.pop(card_index)
        except:
            card_used = self.hand.pop()
        self.discard.append(card_used)
        self.question_area.addQuestion(card_used,rowsdown)

    def turnStart(self):
        self.frame.grid(column=0,row=8,columnspan=6,rowspan=3,sticky=N)
        for child in self.frame.winfo_children():
            child.configure(state='normal') #turns each component of frame on, so that users can see it

    def endCardChoice(self):
        for child in self.frame.winfo_children():
            child.configure(state='disable') #turns each component off
        for i in range(0,5):
            match self.cards_to_play[i].get():
                case True:
                    self.play(card_index=i,rowsdown=i)
        self.draw()
        
