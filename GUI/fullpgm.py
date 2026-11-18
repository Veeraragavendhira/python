# from tkinter import *
# root = Tk()
# root.title("Login Form")
# root.geometry("500x500")
# Label(root, text="Username").pack()
# username = Entry(root)
# username.pack()
# Label(root, text="Password").pack()
# password = Entry(root, show="*")
# password.pack()
# Label(root, text="Comments").pack()
# comment = Text(root, height=4, width=25)
# comment.pack()
# listbox = Listbox(root)
# listbox.insert(1, "Admin")
# listbox.insert(2, "Student")
# listbox.insert(3, "Guest")
# listbox.pack()
# Button(root, text="Login").pack()
# root.mainloop()


import tkinter as tk
from tkinter import messagebox
import sqlite3

# ---------------- DATABASE ---------------- #

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    username TEXT PRIMARY KEY,
    password TEXT
)
""")
    
conn.commit()

# ---------------- FUNCTIONS ---------------- #

def register():

    username = entry_username.get()
    password = entry_password.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "Fill all fields")
        return

    try:
        cursor.execute("INSERT INTO users VALUES(?,?)", (username, password))
        conn.commit()
        messagebox.showinfo("Success", "Registration Successful")
    except:
        messagebox.showerror("Error", "Username Already Exists")


def login():

    username = entry_username.get()
    password = entry_password.get()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Success", f"Welcome {username}")
    else:
        messagebox.showerror("Failed", "Invalid Username or Password")


def clear():
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Login System")
root.geometry("400x320")
root.resizable(False, False)

title = tk.Label(
    root,
    text="LOGIN PAGE",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)

lbl1 = tk.Label(root, text="Username")
lbl1.pack()

entry_username = tk.Entry(root, width=30)
entry_username.pack(pady=5)

lbl2 = tk.Label(root, text="Password")
lbl2.pack()

entry_password = tk.Entry(root, width=30, show="*")
entry_password.pack(pady=5)

login_btn = tk.Button(
    root,
    text="Login",
    width=20,
    bg="green",
    fg="white",
    command=login
)
login_btn.pack(pady=10)

register_btn = tk.Button(
    root,
    text="Register",
    width=20,
    bg="blue",
    fg="white",
    command=register
)
register_btn.pack()

clear_btn = tk.Button(
    root,
    text="Clear",
    width=20,
    command=clear
)
clear_btn.pack(pady=10)

root.mainloop()

conn.close()