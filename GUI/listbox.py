from tkinter import *
root = Tk()
listbox = Listbox(root)
listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C++")
listbox.pack()
root.mainloop()
# print(listbox.get(listbox.curselection()))
