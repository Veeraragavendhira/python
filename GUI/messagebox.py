from tkinter import *
from tkinter import messagebox
root = Tk()
def info():
    messagebox.askyesno("note", "Login Successful")
Button(root, text="Login", command=info).pack()
root.mainloop()
