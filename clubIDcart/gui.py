import tkinter as tk
from typing import Text 
from tkinter import messagebox
from tkcalendar import DateEntry 
import uuid

class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        tk.Label(self , text = "First Name" ).grid(row = 0 , column = 0)
        self.name = tk.StringVar()
        tk.Entry(self , textvariable=self.name).grid(row = 0 , column = 1)

        tk.Label(self , text = "Last Name" ).grid(row = 1 , column = 0)
        self.last = tk.StringVar()
        tk.Entry(self , textvariable=self.last).grid(row = 1 , column = 1)
   
        tk.Label(self , text = "Birth Data" ).grid(row = 2 , column = 0)
        self.birthdata = tk.StringVar()
        DateEntry(self , textvariable=self.birthdata,
        date_pattern = "y-mm-dd", 
        background="#81ecec",
        foreground="white" , bordercolor = "#81ecec" ,
        headersbackground = "white").grid(row = 2 , column = 1)

        tk.Button(self , text= "Create" , command= self.create).grid(row = 3 , column=0 ,columnspan=2 , sticky=tk.E+tk.W)

        # tk.Label(self , text = "Club Id" ).grid(row = 3 , column = 0)
        # self.clubID = tk.StringVar()
        # tk.Entry(self,textvariable= self.clubID).grid(row = 3 , column = 1)

        # tk.Label(self , text = "Image" ).grid(row = 4 , column = 0)
        # self.image = tk.StringVar()
        # tk.Entry(self,textvariable= self.image).grid(row = 4 , column = 1)

    def create(self):
        print(self.name.get() , self.last.get() , self.birthdata.get(),self.get_id())
        messagebox.showinfo( "Done", "Successful")

    def get_id(self):
        return int(uuid.uuid1().int/100000000000000000000)
    
    def main(self):
        self.mainloop()        