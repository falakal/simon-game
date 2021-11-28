from tkinter import *
from tkinter import messagebox
root = Tk()
def login():
    username=Username.get()
def login_window():
    root.title("login")
    root.geometry("300x200")
    global Username
    Label(root, text="Username:").place(x=20, y=20)
    Username = Entry(root, bd=5)
    Username.place(x=140, y=20)

login_window()
Button(root,text="Login",command=login,heigh=2,width=12,bd=3).place(x=30,y=80)
root.mainloop()