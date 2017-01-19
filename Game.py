from Tkinter import *
from random import randint
import tkMessageBox

import time

class Application(Frame):
    """Radio Button"""
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
        

    def create_widgets(self):
        self.check = IntVar()
        Label(self,text="Please pick the game you want!!").grid(row =0,column =0, sticky=W)
        self.chk1 =Checkbutton(self,
                    text="Guess the number between 0 ~ 100 ",
                    variable =self.check,
                    onvalue = 1,
                    offvalue = 0,
                    command = self.game1_start
                    )
        self.chk1.grid(row =1,column =0, sticky=W)
    def game1_start(self):
        """show the result in the text widget"""
        self.window = Toplevel(self)
        self.window.title("1~100 small game")
        self.Max =100
        self.Min =0
        self.random =randint(0,100)
        self.label = Label(self.window,text = "Please enter a number between "+str(self.Min)+" ~ "+str(self.Max)+"    ")
        self.label.grid(row=2, column =0, sticky =W)
        self.number = Entry(self.window)
        self.number.grid(row=2, column =1, sticky =W)
        self.submit = Button(self.window, text = "submit", command =self.process1)
        self.submit.grid(row = 2,column = 2, sticky =W)
        self.result= Text(self.window,
                          width = 50,
                          heigh = 20,
                          wrap =WORD)
        self.result.grid(row =5,column =0, columnspan =3)

    def process1(self):
        """The number typed in to compare"""
        random = int(self.random)
        check =True
        try:
            number = int(self.number.get())
        except(ValueError,TypeError):
            message = "\nYou cannot enter except for integer number!!"
            message += "\nPlease enter the range: "+str(self.Min)+" ~ "+str(self.Max)
            self.result.delete("0.0 ",END)
            self.result.insert("0.0 ",message)
            self.label=Label(self.window,text = "Please enter a number between "+str(self.Min)+" ~ "+str(self.Max)+"   ").grid(row=2, column =0, sticky =W)
        else:
            self.number.delete(0,END)
            if number < random and number <=self.Max and number >=self.Min:
                self.Min = number
                message = "\nNew range is "+str(self.Min)+" ~ "+str(self.Max)
                self.result.delete("0.0 ",END)
                self.result.insert("0.0 ",message)
                self.label=Label(self.window,text = "Please enter a number between "+str(self.Min)+" ~ "+str(self.Max)+"   ").grid(row=2, column =0, sticky =W)
            elif number > random and number <= self.Max and number >=self.Min :
                self.Max =number
                message = "\nNew range is "+str(self.Min)+" ~ "+str(self.Max)
                self.result.delete("0.0 ",END)
                self.result.insert("0.0 ",message)
                self.label=Label(self.window,text = "Please enter a number between "+str(self.Min)+" ~ "+str(self.Max)+"   ").grid(row=2, column =0, sticky =W)
            elif number == random :
                check = False
                tkMessageBox.showinfo(title = "Game Over",message = "You win!!")
                self.chk1.deselect()
                self.window.destroy()
            else :
                message ="\nPlease enter a  valid number between "+str(self.Min)+" ~ "+str(self.Max)
                self.result.delete("0.0 ",END)
                self.result.insert("0.0 ",message)
                self.label=Label(self.window,text = "Please enter a number between "+str(self.Min)+" ~ "+str(self.Max)+"   ").grid(row=2, column =0, sticky =W)

            
        
       

   


#main
root = Tk()
root.title("Game")
root.geometry("300x500")
app = Application(root)

root.mainloop()
        
        
        
