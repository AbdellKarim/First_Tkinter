from tkinter import *
from tkinter import ttk
import datetime
import time



class Student_graph():
    def __init__(self, master ):
        self.master = master
        self.size_of_width = 20

        
    def the_timetable_button(self , master):
        

                                                                            #Label its Title of Programme
        self.title_general= Label(master , text = "Programme For Student")
        self.title_general.config(font = ('courier', 20 , 'bold'))
      #  self.title_general.grid_location(40, 40)
        self.title_general.grid(row = 0 , column = 0,columnspan = 2 , ipadx  = 5)
        self.title_general.config(font=('helvetica', 20, 'underline italic'))
        
                                                                            #juste Button empty for The Timetable
        self.buttonn_The_Timetable = ttk.Button(master, text = "The Timetable", width = self.size_of_width)
        self.buttonn_The_Timetable.grid(row = 1 , column = 0, ipady=30)
        #self.buttonn_The_Timetable.config(font=('helvetica', 20, 'underline italic'))
        
                                                                            #auther Button empty
        self.buttonn_Point = ttk.Button(master, text = "Point", width = self.size_of_width)
        self.buttonn_Point.grid(row = 2 , column = 0,ipady=30)
        
                                                                    #auther Button empty
        self.buttonn_exercises = ttk.Button(master, text = "exercises", width = self.size_of_width)
        self.buttonn_exercises.grid(row = 3 , column = 0,ipady=30)
                                                                        #auther Button empty
        
        self.buttonn_Note = ttk.Button(master, text = "Note", width = self.size_of_width)
        self.buttonn_Note.grid(row = 4 , column = 0,ipady=30)
        
    def Informtion_date(self, master):
        #date information in title genral of the programme
        

        datea= time.asctime( time.localtime(time.time()) )
        
     
  
        
        self.Labeltime0 =Label(master , text =datea)    
        self.Labeltime0.place(x = 210 , y= 80)
        #self.Labeltime0.grid(row= 1,  column = 2 , columnspan =2, sticky  ="W")
        self.Labeltime0.config(font=(('Lato Medium', 11 , 'bold')))
       # self.Labeltime0.config(wraplength = 120)
  
        self.Labeltime = Label(master, text = "Date  :")
        self.Labeltime.grid(row= 1,  column = 1, columnspan = 2,sticky = "NW")
        self.Labeltime.config(font=(('OpenDyslexic', 11 , 'bold')))
        
    def information_personnel(self, master):
        
        # information like num prenom year pucture personell ,,,,
        self.name = Label(master, text = "Nom  :")
        self.name.grid(row = 2 , column = 1,sticky = "NW")#desactive this confih to see the difrent'''sticky = "NW"
        self.name1 = Label(master, text = "Abd lkarim")
        self.name1.grid(row = 2 , column = 1, sticky = "E")
        
        
        
        self.prenom = Label(master, text = "prenom  :")
        self.prenom.grid(row = 3 , column = 1,sticky = "NW")
        self.prenom = Label(master, text = "Bennasser")
        self.prenom.grid(row = 3 , column = 1, sticky = "E")
        
    
    def Image(self, master):
        
           puctu_myself =PhotoImage(file = '130.gif').subsample(20, 20)
           self.label = Label(master,compound = CENTER, image=puctu_myself)
         #  self.label.grid(row=3, column=1, columnspan=2, rowspan = 2)
           self.label.place(x =210, y = 210)
        
    
def main():
    root = Tk()
    root.geometry("440x480+50+50")

    student= Student_graph(root)
    student.the_timetable_button(root)
    student.Informtion_date(root)
    student.information_personnel(root)
    

  #  img = PhotoImage(file='student.gif')
    student.Image(root)


    
    root.mainloop()


    
if __name__ == '__main__': main()
        
    
