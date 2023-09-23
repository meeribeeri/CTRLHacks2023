import tkinter

class Question_Text():
    def __init__(self,question : str, frame : tkinter.Frame):
        self.question = question
        self.label = tkinter.Label(frame,question,anchor="center")