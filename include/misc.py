import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *

from include.card import Card
from include.player import Player


class Question_Text():
    def __init__(self,question : str, frame : Frame):
        self.question = question
        self.label = Label(frame,question,anchor="center")

class Question_Box():
    def __init__(self,master : Tk):
        self.master = master
        self.targets = []#recievers of damage
        self.current_target = 0 #current reciever

        self.frame = Frame(master)
        self.frame['borderwidth'] = 2
        self.frame['relief'] = 'sunken'
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid(row=1,column=0,columnspan=6,rowspan=7,sticky=N)
        self.questions = []

        self.title = Label(master=self.frame,text="Answer All Questions")
        self.title.grid(row=0,column=0,columnspan=6,sticky=N)

        self.final_answer = Button(master=self.frame,text="Finish",command=self.finalize)
        self.final_answer.grid(row=7,column=0,columnspan=6,sticky=N)
        self.restart = False

    def addQuestion(self,question : Card,rowsdown : int = 0):
        self.questions.append(question)
        self.questions[-1].play(self.frame,rowsdown)

    def retarget(self,new_target : int):
        self.current_target = new_target

    def finalize(self):
        damage = 0
        self_damage = 0
        for card in self.questions:
            if card.mc_question.chosen.get() == card.mc_question.answer:
                damage = damage + (5 * card.difficulty)
            else:
                self_damage = self_damage + int(2.5 * card.difficulty)
        for question in self.questions:
            question.mc_question.delete()
        
        self.questions = []


        self.title = Label(master=self.frame,text="Answer All Questions")
        self.title.grid(row=0,column=0,columnspan=6,sticky=N)

        self.final_answer = Button(master=self.frame,text="Finish",command=self.finalize)
        self.final_answer.grid(row=7,column=0,columnspan=6,sticky=N)

        self.targets[self.current_target].damage(damage)
        self.targets[self.current_target-1].damage(self_damage)
        self.targets[self.current_target-1].turnEnd()
        self.targets[self.current_target].turnStart()
        print(len(self.targets[self.current_target].deck))
        match self.current_target:
            case 0:
                self.retarget(1)
            case _:
                self.retarget(0)

        for player in self.targets:
            if player.hp <= 0:
                self.master.quit()
                
        
    def delete(self):
        for child in self.frame.winfo_children():
            child.destroy()
        self.frame.destroy()

