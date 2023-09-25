import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *

from include.menu import TopBar

class Question_Text(): #Literally just a label for containing a question... not sure why we didn't just... y'know... label it normally... like we did before... Welp too late now
    def __init__(self,question : str, frame : Frame):
        self.question = question
        self.label = Label(frame,question,anchor="center")
        
class Question_Box(): #Area containing all played questions
    def __init__(self,master : Tk):
        self.master = master#window
        self.targets = []#recievers of damage
        self.current_target = 0 #current reciever
        self.top_bar = None #topbar, filled later

        self.frame = Frame(master) #Frame containing everything
        self.frame['borderwidth'] = 2
        self.frame['relief'] = 'sunken'
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(5, weight=1)
        self.frame.grid(row=1,column=1,columnspan=1,rowspan=7,sticky=N+E+W)
        self.questions = [] #All current questions
        self.previous_questions = [] #Whether the question answers were correct or not

        self.title = Label(master=self.frame,text="Answer All Questions") #Top label(mini title)
        self.title.grid(row=0,column=0,columnspan=6,sticky=N)

        self.final_answer = Button(master=self.frame,text="Finish",command=self.finalize) #Finish button
        self.final_answer.grid(row=7,column=0,columnspan=6,sticky=N)
        self.final_answer.configure(state="disable") #Disabled so players cant just... press the answer button before they play anything

    def addQuestion(self,question,rowsdown : int = 0): #Used to add a question to the area
        self.questions.append(question)
        self.questions[-1].play(self.frame,rowsdown)

    def get_topbar(self,topbar : TopBar): #literally just a function to deal with the circular parameter thing I made and have to deal with
        self.top_bar = topbar

    def retarget(self,new_target : int): #Retarget who is taking damage
        self.current_target = new_target

    def finalize(self): #Finalize answers & logic
        damage = 0 #damage to target
        self_damage = 0 #Self damage on incorrect answer
        self.final_answer.configure(state='disabled') #Redisable finalize button
        for card in self.questions: #Logic to add to damage/self damage depending on answer
            if card.mc_question.chosen.get() == card.mc_question.answer:
                damage = damage + (5 * card.difficulty)
                self.previous_questions.append(True)
            else:
                self_damage = self_damage + int(2.5 * card.difficulty)
                self.previous_questions.append(False)
        self.top_bar.update() #Update top bar's previous answer thingy
        for question in self.questions: #Delete last questions
            question.mc_question.delete()
        
        self.questions = []
        self.previous_questions = [] #Wipe clean for next time

        #Damage applied to players
        self.targets[self.current_target].damage(damage)
        self.targets[self.current_target-1].damage(self_damage)

        self.targets[self.current_target-1].turnEnd() #End current player's turn
        self.targets[self.current_target].turnStart() #Start next player's turn
        match self.current_target: #Properly retarget self
            case 0:
                self.retarget(1)
            case _:
                self.retarget(0)

        for player in self.targets: #Check to see if anybody won
            if player.hp <= 0:
                self.master.quit() #Exit window mainloop, continued in main.py
                
        
    def delete(self): #Delete self from window
        for child in self.frame.winfo_children():
            child.destroy()
        self.frame.destroy()

    def activate(self): #Reactivate the final answer button
        self.final_answer.configure(state='normal')

