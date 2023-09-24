import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *

from include.card import Card

class Question_Text():
    def __init__(self,question : str, frame : Frame):
        self.question = question
        self.label = Label(frame,question,anchor="center")

class Question_Box():
    def __init__(self,master : Tk):
        self.master = master
        self.frame = Frame(master)
        self.frame['borderwidth'] = 2
        self.frame['relief'] = 'sunken'
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid(row=1,column=1,columnspan=6,rowspan=7,sticky=N)
        self.questions = []

        self.title = Label(master=self.frame,text="Answer All Questions")
        self.title.grid(row=0,column=0,columnspan=6,sticky=N)

        self.final_answer = Button(master=self.frame,text="Finish",command=self.finalize)
        self.final_answer.grid(row=7,column=0,columnspan=6,sticky=N)

    def addQuestion(self,question : Card,rowsdown : int = 0):
        self.questions.append(question)
        question.play(self.frame,rowsdown)

    def finalize(self):
        damage = 0
        self_damage = 0
        for card in self.questions:
            if card.mc_question.chosen == card.mc_question.answer:
                damage = damage + (5 * card.difficulty)
            else:
                self_damage = self_damage + int(2.5 * card.difficulty)
        for child in self.frame.winfo_children():
            if child.winfo_class() in ('Frame'):
                child.destroy()