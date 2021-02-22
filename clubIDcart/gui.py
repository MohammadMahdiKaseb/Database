import tkinter as tk
from typing import Text 
from tkinter import messagebox
from sqlalchemy.sql.functions import random
from tkcalendar import DateEntry 
import random
from tkinter import filedialog
from DataBase.connection import Connection
from DataBase.models import Member



ft = {"bg" : "#392F5A" , "fg" : "#FF8811" }
fb = {"bg" : "#F4E0CA" }

class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        

        #######################################################################

        frame_r = tk.LabelFrame(self , text= "Register" , cnf=fb)
        frame_r.grid(row=0 , column=0)
        
        tk.Label(frame_r , text = "First Name" , cnf=ft).grid(row = 0 , column = 0)
        self.name = tk.StringVar()
        tk.Entry(frame_r , textvariable=self.name).grid(row = 0 , column = 1)

        tk.Label(frame_r , text = "Last Name", cnf=ft ).grid(row = 1 , column = 0)
        self.last = tk.StringVar()
        tk.Entry(frame_r , textvariable=self.last).grid(row = 1 , column = 1)
   
        tk.Label(frame_r , text = "Birth Data" , cnf=ft).grid(row = 2 , column = 0)
        self.birthdata = tk.StringVar()
        DateEntry(frame_r , textvariable=self.birthdata,
        date_pattern = "y-mm-dd", 
        background="#81ecec",
        foreground="white" , bordercolor = "#81ecec" ,
        headersbackground = "white").grid(row = 2 , column = 1)

        tk.Button(frame_r , text= "Create" , command= self.create).grid(row = 4 , column=0 ,columnspan=2 , sticky=tk.E+tk.W)

        tk.Label(frame_r , text = "Image", cnf=ft ).grid(row = 3 , column = 0)
        self.filename = tk.StringVar()
        tk.Button(frame_r , text= "Browse" , command= self.browse_func).grid(row = 3 , column=1 ,columnspan=2 , sticky=tk.E+tk.W)

        #######################################################################

        frame_d = tk.LabelFrame(self , text= "Delete")
        frame_d.grid(row=1 , column=0)

        self.id_del = tk.IntVar()
        tk.Entry(frame_d , textvariable=self.id_del).grid(row = 0 , column = 0)
        tk.Button(frame_d , text= "Delete" , command= self.delete_func).grid(row = 0 , column=1)
        

     
        #######################################################################
        
        frame_u = tk.LabelFrame(self , text= "Update" , cnf=fb)
        frame_u.grid(row=0 , column=1)

        tk.Label(frame_u , text = "ID", cnf=ft ).grid(row = 0 , column = 0)
        self.id_u = tk.StringVar()
        tk.Entry(frame_u , textvariable=self.id_u).grid(row = 0 , column = 1)
        
        tk.Label(frame_u , text = "First Name" , cnf=ft).grid(row = 1 , column = 0)
        self.name_u = tk.StringVar()
        tk.Entry(frame_u , textvariable=self.name_u).grid(row = 1 , column = 1)

        tk.Label(frame_u , text = "Last Name", cnf=ft ).grid(row = 2 , column = 0)
        self.last_u = tk.StringVar()
        tk.Entry(frame_u , textvariable=self.last_u).grid(row = 2 , column = 1)
   
        tk.Label(frame_u , text = "Birth Data" , cnf=ft).grid(row = 3 , column = 0)
        self.birthdata_u = tk.StringVar()
        DateEntry(frame_u , textvariable=self.birthdata_u,
        date_pattern = "y-mm-dd", 
        background="#81ecec",
        foreground="white" , bordercolor = "#81ecec" ,
        headersbackground = "white").grid(row = 3 , column = 1)

        tk.Label(frame_u , text = "Image", cnf=ft ).grid(row = 4 , column = 0)
        self.filename_u = tk.StringVar()
        tk.Button(frame_u , text= "Browse" , command= self.browse_func).grid(row = 4 , column=1)

        tk.Button(frame_u , text= "Update" , command= self.create).grid(row = 5 , column=0 ,columnspan=2 , sticky=tk.E+tk.W)
    #######################################################################

    def up(self):
        session = Connection().create_session()
        person = session.query(Member).filter(Member.memberID == self.id_del.get())
        person.update({
            "first_name":self.name_u.get(),
            "last_name":self.last_u.get(),
            "image":self.filename_u.get(),
            "first_name":self.name_u.get(),
        })
    def browse_func(self):
        self.filename.set(filedialog.askopenfilename())

    
    def delete_func(self):
        session = Connection().create_session()
        person = session.query(Member).filter(Member.memberID == self.id_del.get())
        person.delete()
        session.commit()
        messagebox.showinfo( "Done", "Was deleted")


    def create(self):
        name = self.name.get()
        last = self.last.get()
        image = self.filename.get()
        birth = self.birthdata.get()
        id_ = self.get_id()
        
        session = Connection().create_session()
        member = Member(name , last , id_ , birth , image)
        
        session.add(member)
        session.commit()

        messagebox.showinfo( "Done", "Successful")

    def get_id(self):
        return random.randint(1 , 1000)
    
    #######################################################################    
    
    def main(self):
        self.mainloop()        