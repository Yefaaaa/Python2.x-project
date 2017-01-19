from Tkinter import *
from random import randint
import tkMessageBox
import ttk


import time

class Application(Frame):
    """Radio Button"""
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
        

    def create_widgets(self):
        self.check1 = IntVar()
        self.check2 = IntVar()
        Label(self,text="Please pick the one you want!!").grid(row =0,column =0, sticky=W)
        self.chk1 =Checkbutton(self,
                    text="Guess the number between 0 ~ 100 ",
                    variable =self.check1,
                    onvalue = 1,
                    offvalue = 0,
                    command = self.game1_start
                    )
        self.chk1.grid(row =1,column =0, sticky=W)
        self.chk2 =Checkbutton(self,
                    text="This is a Survay form! ",
                    variable =self.check2,
                    onvalue = 1,
                    offvalue = 0,
                    command = self.survay_start
                    )
        self.chk2.grid(row =2,column =0, sticky=W)
        
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

    def survay_start(self):
        self.w1 = Toplevel(self)
        self.w1.title("Survay Form")
        self.w1.resizable(False,False)
        self.w1.configure(background ="#e1d8b9")
        self.style =ttk.Style()
        self.style.configure("TFrame",background ="#e1d8b9")
        self.style.configure("TButton",background ="#e1d8b9")
        self.style.configure("TLabel",background ="#e1d8b9")





        
        self.logo =PhotoImage(file = "/Users/yefamai/Desktop/logo.gif")
        ttk.Label(self.w1,image = self.logo).grid(row =0,column =0)
        
        ttk.Label(self.w1,
                  text = "Please fill the survay! Thank you!",background ="blue",
                  font =("Arial",24)).grid(
                      row =0, column=1,columnspan =3)
        
        ttk.Label(self.w1,text ="Name :",background ="blue").grid(row =1,column =0)
        self.name = ttk.Entry(self.w1)
        self.name.grid(row = 1,column=1,columnspan =2)
        
        ttk.Label(self.w1,text ="Email :",background ="blue").grid(row =2,column =0)
        self.email = ttk.Entry(self.w1)
        self.email.grid(row = 2,column=1,columnspan =2)
        
        ttk.Label(self.w1,text ="Comment :",background ="blue").grid(row =3,column =0,stick ="en")
        self.comment =Text(self.w1,width =40,heigh=10,wrap ="word")
        self.comment.grid(row=3,column=1,columnspan =2)
        scrollbar= ttk.Scrollbar(self.w1,orient = VERTICAL,
                         command = self.comment.yview)
        scrollbar.grid(row=3,column=4,sticky ="ns")
        self.comment.configure(yscrollcommand = scrollbar.set)

        self.frame =ttk.Frame(self.w1)
        self.frame.grid(row =4,column =0,columnspan =4)
        submit = ttk.Button(self.frame,text = "submit",command=self.submit)
        submit.pack(side= LEFT)
        clear = ttk.Button(self.frame,text = "clear",command =self.clear)
        clear.pack(side= LEFT)
        eixt = ttk.Button(self.frame,text = "exit",command =self.exit_)
        eixt.pack(side= LEFT)

    def exit_(self):
        self.chk2.deselect()
        self.w1.destroy()


    def clear(self):
        self.name.delete(0,END)
        self.email.delete(0,END)
        self.comment.delete("0.0",END)

    def submit(self):
        self.message = "    Name:"+ self.name.get()+" \n"
        self.message +="   Email:"+ self.email.get()+" \n"
        comment = str(self.comment.get("0.0",END))
        
        message = ""
        for char in comment:
            if char != "\n":
                message +=char
            else :
                message +="\n"
                message += "         "
        self.message += "Comment :"+ message
        self.message +="\n"
        self.store()
        self.name.delete(0,END)
        self.email.delete(0,END)
        self.comment.delete("0.0",END)

    def store(self):
        with open("Survay.txt","a") as outFile:
            outFile.write(self.message)
        outFile.close()

#main
root = Tk()
root.title("Main Selection")
root.geometry("300x500")
app = Application(root)

root.mainloop()
        
        
        
