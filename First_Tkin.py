from tkinter import * 
from tkinter import Toplevel
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox

import datetime
import time



class Student_graph():
    
    
    def __init__(self, master ):
         
        self.master = master
        self.size_of_width = 20
        global maxinumber_of_note 
        global strat_note 
        

    

        
    def the_timetable_button(self , master):
        

                                                                            #Label its Title of Programme
        self.title_general= Label(master , text = "Programme For Student")
        self.title_general.config(font = ('courier', 20 , 'bold'))
      #  self.title_general.grid_location(40, 40)
        self.title_general.grid(row = 0 , column = 0,columnspan = 2 , ipadx  = 5)
        self.title_general.config(font=('helvetica', 20, 'underline italic'))
        
                                                                            #juste Button empty for The Timetable
        self.buttonn_The_Timetable = ttk.Button(master, text = "The Timetable", width = self.size_of_width
                                                , command =  lambda :Student_graph.the_timetablee(self))
        self.buttonn_The_Timetable.grid(row = 1 , column = 0, ipady=30)
        #self.buttonn_The_Timetable.config(font=('helvetica', 20, 'underline italic'))
        
                                                                            #auther Button empty
        self.buttonn_Point = ttk.Button(master, text = "Point", width = self.size_of_width ,
                                        command =  lambda :Student_graph.Point(self, master))
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
        
        self.prenom = Label(master, text = "Class :")
        self.prenom.grid(row = 4 , column = 1,sticky = "NW")
        self.prenom = Label(master, text = "2Bac PC")
        self.prenom.grid(row = 4 , column = 1, sticky = "E")
        
    
    def Image(self, master):
        

            photo = PhotoImage(file = "130.gif").subsample(10, 10)
    
            self.label = Label(image=photo)
            self.label.image = photo 
            self.label.grid(row=2, column=2, columnspan=2,sticky='E')
            self.label.place(x =360, y = 130)
            
    def Point(self, master):

            #add Top level firste cadre for develope point 
        self.Top_level = Toplevel(master)

        self.Top_level.maxsize(640 , 400)
        self.Top_level.minsize(400, 350)
 
       # fondution netbook for cree Frame and add Information inder the frame
        self.newtbook_information = ttk.Notebook(self.Top_level)
        self.newtbook_information.grid()
       
       #the frame 
        self.frame1 = ttk.Frame(self.newtbook_information)
        self.frame2 = ttk.Frame(self.newtbook_information)
       
        self.newtbook_information.add(self.frame1 , text = 'Information')
        self.newtbook_information.add(self.frame2 , text = 'Information')
       
       
       
       
       #menu fore cre information or add information in the programme 


        self.Top_level.title("Simple menu")
        Top = self.Top_level
        self.menubar = Menu(Top)
        Top['menu'] = self.menubar
        self.menu = Menu(self.menubar)
        self.menubar.add_cascade(label="File", menu=self.menu)
        self.menu.add_command(label = 'New' , command= lambda:Student_graph.cree_netbook(self, master))
        self.menu.add_command(label = 'Exit' , command= lambda: print(''))




    def cree_netbook(self, master):  #cree loop Netbook 
        print("sasa")
        maxinumber_of_note = 50
        strat_note = 0
    #    while strat_note <maxinumber_of_note :
    #       start_note = strat_note + 1
           
     #      if start_note == maxinumber_of_note :
     #          messagebox.showinfo("the Note Was Pliented", "you must delete some Note")
               
        self.framea = Toplevel(master)
        self.framea.config(width= 150 , height= 150)
        Top = self.framea
        #Top['Toplevel'] = self.framea
        self.label = Label(Top, text= 'File :')
        self.label.grid(row = 0 , column = 0,sticky = "NW")
        self.label1 = Label(Top, text= 'creat new file')
        self.label1.grid(row = 0 , column = 1, sticky = "WENS")
                                                                                        #title
        self.label1 = Label(Top, text= 'Title')
        self.label1.grid(row = 1 , column =0 , sticky = "E")
        
        self.entre = ttk.Entry(Top, width = 50)
        self.entre.grid(row = 1 ,column = 1)
        
        self.label1 = Label(Top, text= 'Note :')
        self.label1.grid(row = 2 , column = 1, sticky = "WENS")
        
        self.text= Text(Top , width= 60 , height= 20)
        self.text.grid(row = 3 , column = 1)
        
        self.buttoncancel = ttk.Button(Top , text = "Cancel")
        self.buttoncancel.grid(row = 4 , column = 1,ipady=15, sticky = "E" )
        
        
        self.buttoncancel = ttk.Button(Top , text = "Finish")
      #  self.buttoncancel.grid(row = 4 , column = 0,sticky = "WENS",columnspan = 1)
        self.buttoncancel.place(x= 360 , y =387,height =55)
               
        
               
            
               
           
           
        
    

    
            

def main():
    root = Tk()



    root.geometry("440x430+50+50")
    student= Student_graph(root)
    student.the_timetable_button(root)
    student.Informtion_date(root)
    student.information_personnel(root)
    student.Image(root)
   # student.Point(root)

    root.mainloop()


    
if __name__ == '__main__': main()
        
    
