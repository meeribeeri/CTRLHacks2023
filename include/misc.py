import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *

from include.menu import TopBar

class Question_Text():
    def __init__(self,question : str, frame : Frame):
        self.question = question
        self.label = Label(frame,question,anchor="center")
        
class Question_Box():
    def __init__(self,master : Tk):
        self.master = master
        self.targets = []#recievers of damage
        self.current_target = 0 #current reciever
        self.top_bar = None

        self.frame = Frame(master)
        self.frame['borderwidth'] = 2
        self.frame['relief'] = 'sunken'
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(5, weight=1)
        self.frame.grid(row=1,column=1,columnspan=1,rowspan=7,sticky=N+E+W)
        self.questions = []
        self.previous_questions = []

        self.title = Label(master=self.frame,text="Answer All Questions")
        self.title.grid(row=0,column=0,columnspan=6,sticky=N)

        self.final_answer = Button(master=self.frame,text="Finish",command=self.finalize)
        self.final_answer.grid(row=7,column=0,columnspan=6,sticky=N)
        self.final_answer.configure(state="disable")

    def addQuestion(self,question,rowsdown : int = 0):
        self.questions.append(question)
        self.questions[-1].play(self.frame,rowsdown)

    def get_topbar(self,topbar : TopBar): #literally just a function to deal with the circular parameter thing I made and have to deal with
        self.top_bar = topbar

    def retarget(self,new_target : int):
        self.current_target = new_target

    def finalize(self):
        damage = 0
        self_damage = 0
        self.final_answer.configure(state='disabled')
        for card in self.questions:
            if card.mc_question.chosen.get() == card.mc_question.answer:
                damage = damage + (5 * card.difficulty)
                self.previous_questions.append(True)
            else:
                self_damage = self_damage + int(2.5 * card.difficulty)
                self.previous_questions.append(False)
        self.top_bar.update()
        for question in self.questions:
            question.mc_question.delete()
        
        self.questions = []
        self.previous_questions = [] #Wipe clean for next time

        self.targets[self.current_target].damage(damage)
        self.targets[self.current_target-1].damage(self_damage)
        self.targets[self.current_target-1].turnEnd()
        self.targets[self.current_target].turnStart()
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

    def activate(self):
        self.final_answer.configure(state='normal')

