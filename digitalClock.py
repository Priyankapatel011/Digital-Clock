from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")


def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


Label(root, font=("Arial", 30), text="Digital Clock",
      foreground="white", background="black").pack()

label = Label(root, font=("ds-digital", 80),
              background="black", foreground="cyan"
              )
label.pack(anchor="center")
time()

mainloop()