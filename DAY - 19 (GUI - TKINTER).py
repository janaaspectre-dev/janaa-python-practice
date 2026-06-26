#GUI


from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox
main = tk.Tk()
main.geometry("1200x800")
main.title("saTracker")
main.config(bg="cyan")


#LABEL

L = Label(main,font = ("Arial" ,20),fg = "black",bg = "red",text = "Create Account").place(x = 500,y = 100)

nL = Label(main,font = ("Roboto" ,17),fg = "white",bg = "black",text = "Username").place(x = 400,y = 200)
pL = Label(main,font = ("Roboto" ,17),fg = "white",bg = "black",text = "Password").place(x = 400,y = 250)


def show():
    name = ne.get()
    pwd = pe.get()
    place = places.get()
    g = gender.get()
    print("Username:",name)
    print("Password:",pwd)
    print("Place:",place)
    print("Gender:",g)


    
ne = Entry(main)
ne.place(x = 600 , y = 210)
pe = Entry(main)
pe.place(x = 600 , y = 260)

Button(main,text = "submit",command = show).place(x = 500 , y = 400)

places = Combobox(main)
places["values"] = ("Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal")
places.current(0)
places.place(x = 340,y = 340)


gender = StringVar(value = "Male")
rb = Radiobutton(main,text = "Male",variable = gender,value = "Male")
rb.place(x = 300,y = 400)
rb1 = Radiobutton(main,text = "Female",variable = gender , value = "Female")
rb1.place(x = 400,y = 400)
