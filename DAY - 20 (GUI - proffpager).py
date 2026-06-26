from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
page = tk.Tk()
page.geometry("500x600")
page.title("profpage.in")
page.config(bg = "white")


l = Label(page,font =("Helvetica (Bold)",23),fg = "black",bg = "white",text = "Welcom to ProfPager")
q = Label(page,font = ("Roboto(Bold)",21),fg = "black",bg = "white",text = "Sign Up to Continue").place(x = 120,y = 40)
w = Label(page,font = ("Roboto",19),fg = "black",bg = "white",text = "Email")
w.place(x = 90,y = 90)
x = Label(page,font = ("Roboto",19),fg = "black",bg = "white",text = "Password")
x.place(x = 90,y = 120)
v = Label(page,font = ("Roboto",19),fg = "black",bg = "white",text = "Username")
v.place(x=90, y=150)
a = Label(page,font = ("Roboto",19),fg = "black",bg = "white",text = "Age")
a.place(x = 90,y = 180)
c = Label(page,font = ("Roboto",19),fg = "black",bg = "white",text = "Contact Number")
c.place(x = 90,y = 210)
b = Label(page,font = ("Roboto",19),fg = "black",bg = "white",text = "Country")
b.place(x = 90,y = 240)
g = Label(page,font = ("Roboto",19),fg = "black",bg = "white",text = "Gender")
g.place(x = 90,y = 270)
l.pack()

def show():
    email = we.get()
    pwd = xe.get()
    name = ve.get()
    age = ae.get()
    number = ce.get()
    country = places.get()
    g = gender.get()
    print("Email:",email)
    print("Password:",pwd)
    print("Username:",name)
    print("Age:",age)
    print("Contact Number:",number)
    print("Country:",country)
    print("Gender:",g)


we = Entry(page)
we.place(x = 290,y = 95)
xe = Entry(page)
xe.place(x = 290,y = 125)
ve = Entry(page)
ve.place(x = 290,y = 155)
ae = Entry(page)
ae.place(x = 290,y = 185)
ce = Entry(page)
ce.place(x = 290 , y = 220)



Button(page,text = 'Register',command = show).place(x = 200,y = 350)

places = Combobox(page)
places["values"] = ("United States", "China", "Germany", "Japan", "United Kingdom", "India", "France", "Italy", "Russia", "Brazil", "Canada", "Australia", "Mexico", "Spain", "South Korea", "Turkey", "Indonesia", "Netherlands", "Saudi Arabia", "Switzerland", "Poland", "Taiwan", "Ireland", "Belgium", "Sweden", "Israel", "Argentina", "Singapore", "Austria", "United Arab Emirates")
places.current(0)
places.place(x = 290,y = 245)

gender = StringVar(value = "Male")
rb = Radiobutton(page,text = "Male",variable = gender,value = "Male")
rb.place(x = 290,y = 275)
rb1 = Radiobutton(page,text = "Female",variable = gender,value = "Female")
rb1.place(x = 290,y = 295)
rb2 = Radiobutton(page,text = "Others",variable = gender,value = "Others")
rb2.place(x = 290,y = 315)







    
