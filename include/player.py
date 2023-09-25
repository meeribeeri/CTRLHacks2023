from random import randint
import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *
from PIL import ImageTk, Image

from include.menu import TopBar

class Player():
    def __init__(self,question_area,player_num : int = 1,deck : list = None, window : Tk = None, hp : int = 100, max_hp : int = 100,label_column :int = 0):
        self.deck = deck
        self.hand = []
        self.discard = []
        self.question_area = question_area
        self.hp = hp
        self.max_hp = max_hp
        #image
        self.image_ref_base = Image.open('include\Player_Image.png')
        self.image_ref_base = self.image_ref_base.resize((75,150))
        if player_num == 2:
            self.image_ref = self.image_ref_base.transpose(Image.FLIP_LEFT_RIGHT)
        else:
            self.image_ref = self.image_ref_base
        self.image = ImageTk.PhotoImage(self.image_ref)
        #side frame
        self.side_frame = Frame(master=window)
        self.side_frame['borderwidth'] = 2
        self.side_frame['relief'] = 'sunken'
        self.side_frame.grid_rowconfigure(2, weight=1)
        self.side_frame.grid_columnconfigure(0, weight=1)
        self.side_frame.grid(row=7,column=label_column,rowspan=3,sticky=N)

        self.image_label = Label(master = self.side_frame,text=f"Player {player_num}",image=self.image,compound='top')
        self.image_label.grid(row=0,column=0,sticky=N)

        self.hp_str_var = StringVar(value=f"HP : {self.hp}/{self.max_hp}")
        self.hp_label = Label(master=self.side_frame,textvariable=self.hp_str_var)
        self.hp_label.grid(row=1,column=0,sticky=N)
        
        self.cards_to_play = [BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar()]
        self.master = window

        #Question Choice Frame & Components
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
            
    def damage(self,damage : int):
        self.hp-=damage
        self.hp_str_var.set(f"HP : {self.hp}/{self.max_hp}")

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
        self.activate()
        self.frame.grid(column=0,row=11,columnspan=6,rowspan=3,sticky=N)
        for child in self.frame.winfo_children():
            child.configure(state='normal') #turns each component of frame on, so that users can see it

        


    def endCardChoice(self):
        for child in self.frame.winfo_children():
            child.configure(state='disable') #turns each component off
        
        played_card_count = 0
        for i in range(0,5):
            match self.cards_to_play[i].get():
                case True:
                    self.play(card_index=i-played_card_count,rowsdown=i)
                    played_card_count+=1
        self.draw()
        self.question_area.activate()

    def turnEnd(self):
        self.cards_to_play = [BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar()]
        for child in self.frame.winfo_children():
            child.configure(state='disable')

        for component in self.frame_components:
            component.destroy()

        self.frame_components = []

    def activate(self):
        

        for i in range(0,5):
            self.frame_components.append(Label(master=self.frame,text=self.hand[i].text,image=self.hand[i].image,compound=BOTTOM))
            self.frame_components[i*2].grid(row=1,column=i+1,sticky=N)
            self.frame_components.append(Checkbutton(master=self.frame,text="Play",onvalue=True,offvalue=False,variable=self.cards_to_play[i]))
            self.frame_components[i*2+1].grid(row=2,column=i+1,sticky=N)
        self.frame_components.append(Button(master=self.frame,text="Play Cards",command=self.endCardChoice))
        self.frame_components[10].grid(row=3,column=0,columnspan=6,sticky=N)

    def delete(self):
        for child in self.frame.winfo_children():
            child.destroy()

        self.frame.destroy()

