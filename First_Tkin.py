
from tkinter import *
from tkinter import ttk




class Usrr():
    
    def __init__(self, ssl):
        self.ssl = ssl
        
        self.but = Button(ssl, text= "Clicke here")
        self.but.pack()
    


    def Man(self , ssl):
        
        self.sa = ttk.Button(ssl , text = "Hellow")
        self.sa.pack()
    
    
    
root = Tk()
sanp = Usrr(root)
sanp.Man(root)

root.mainloop()
