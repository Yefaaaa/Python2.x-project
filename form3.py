from tkinter import *
from tkinter import ttk


class Feedback(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.window()
        
    def window(self):
        self.logo =PhotoImage(file = "/Users/yefamai/Desktop/logo.gif")
        ttk.Label(self,image = self.logo).grid(row =0,column =0)
        
        ttk.Label(self,
                  text = "Please fill the survay! Thank you!",background ="white").grid(
                      row =0, column=1,columnspan =3)
        
        ttk.Label(self,text ="Name :",background ="white").grid(row =1,column =0)
        self.name = ttk.Entry(self)
        self.name.grid(row = 1,column=1,columnspan =2)
        
        ttk.Label(self,text ="Email :",background ="white").grid(row =2,column =0)
        self.email = ttk.Entry(self)
        self.email.grid(row = 2,column=1,columnspan =2)
        
        ttk.Label(self,text ="Comment :",background ="white").grid(row =3,column =0,stick ="en")
        self.comment =Text(self,width =40,heigh=10,wrap ="word")
        self.comment.grid(row=3,column=1,columnspan =2)
        scrollbar= ttk.Scrollbar(self,orient = VERTICAL,
                         command = self.comment.yview)
        scrollbar.grid(row=3,column=4,sticky ="ns")
        self.comment.configure(yscrollcommand = scrollbar.set)
        
        submit = ttk.Button(self,text = "submit",command=self.submit)
        submit.grid(row =4,column =0,columnspan =2)
        clear = ttk.Button(self,text = "clear",command =self.clear)
        clear.grid(row =4,column =2,columnspan =2)

       

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
            
def main():             
    root = Tk()
    root.geometry("480x640")
    root.title("Survay Form")
    feedback = Feedback(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()
