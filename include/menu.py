import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *

class TopBar(): #Stuff at the top of the screen
    def __init__(self,master : Tk,question_area):
        self.master = master #Window
        self.box = question_area #Question area,not casted in parameters to avoid circular import
        self.frame = Frame(master=master) #frame containing everything
        self.frame['borderwidth'] = 2
        self.frame['relief'] = 'sunken'
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid(row=0,column=0,columnspan=8,sticky=N+E+W)

        self.title = Label(master=self.frame,text="Study Card Duels") #Title
        self.title.grid(row=0,column=1,columnspan=6,sticky=N)

        #A bit of text below the title telling the players what they got wrong last time
        self.answer_text = "Previous Answers: " 
        for ans in self.box.previous_questions:
            if ans:
                self.answer_text = self.answer_text + "O "
            else:
                self.answer_text = self.answer_text + "X "
        self.ans_var = StringVar(value=self.answer_text)
        self.mid_label = Label(master=self.frame,textvariable=self.ans_var)
        self.mid_label.grid(row=1,column=1,sticky=N+E+W)

        #Legend for telling what answer was correct or not
        self.bottom_label = Label(master=self.frame,text="O = Correct Answer, X = Incorrect Answer, Left-most was the answer to the top-most question, Right-most was the answer to the bottom-most")
        self.bottom_label.grid(row=2,column=1,columnspan=6,sticky=N+E+W)

    def delete(self): #delete self from window
        self.title.destroy()
        self.frame.destroy()

    def update(self): #update the bit of text telling players what they got wrong
        self.answer_text = "Previous Answers: " 
        for ans in self.box.previous_questions:
            if ans:
                self.answer_text = self.answer_text + "O "
            else:
                self.answer_text = self.answer_text + "X "
        self.ans_var.set(self.answer_text)

class EndScreen(): #The restart/quit screen when somebody wins
    def __init__(self,master : Tk,winner : int):
        self.master = master #window

        self.frame = Frame(master = master) #Frame containing everything
        self.frame['borderwidth'] = 2
        self.frame['relief'] = 'sunken'
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid(row=0,column=0,columnspan=6,rowspan=2,sticky=N+E+W)
        self.text = f"Player {winner} wins!"

        self.end_text = Label(master=self.frame,text=self.text) #Label to tell players who won
        self.end_text.grid(row=0,column=0,sticky=N+S)

        self.restart_button = Button(master=self.frame,text="Restart",command=self.restart) #Button to restart
        self.restart_button.grid(row=1,column=0,sticky=N)
        
        self.exit_button = Button(master=self.frame,text="Exit",command=exit) #button to exit, calls the exit function to leave the program
        self.exit_button.grid(row=2,column=0,sticky=N)

    def restart(self): #Restart function
        for child in self.frame.winfo_children(): #delete self
            child.destroy()
        self.frame.destroy()
        self.master.quit() #exit window mainloop, which will continue in main.py

    def delete(self):
        #delete self
        self.frame.destroy()

