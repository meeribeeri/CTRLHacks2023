import tkinter


class equation():
    def __init__(self,cards : list):
        self.cards = cards
        self.answer = 0
        for card in self.cards:
            match card.value:
                case "+":
                    self.answer+=card.num
                case "-":
                    self.answer-=card.num
                case "*":
                    self.answer*=card.num
                case "/":
                    self.answer/=card.num
                case "^":
                    self.answer = self.answer ** card.num
                case "||":
                    self.answer = abs(self.answer)
    
    def display(self,window : tkinter.Tk):
        pass