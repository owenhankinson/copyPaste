from tkinter.constants import CENTER, END, INSERT, LEFT, RAISED, RIGHT, SINGLE, TOP
from tkinter import Button, Label, Message, Scrollbar, StringVar, Text, Listbox
import tkinter
import time
import keyboard as kb
import pyperclip
from utils import lst


app = tkinter.Tk()
app.title("copyPaste")
app.geometry("500x300")

lstbox_widget = Listbox(
    app,
    justify=LEFT,
    selectmode=SINGLE,
)

def resetList():
    lstbox_widget.delete(0,END)
    global lst
    lst.clear()


def make_clipboard():
    print("Appending to lst")
    clipboard = app.clipboard_get()
    lst.append(clipboard)
    for entry in lst:
        lstbox_widget.insert(END, entry)
    print(lst)


button = Button(
    app,
    justify=RIGHT,
    text="Start", 
    #command=startThread
)

button2 = Button(
    app,
    justify=RIGHT,
    text="paste", 
    #command=startThread2
)

resetButton = Button(
    app,
    justify=RIGHT,
    text="Reset List",
    command=resetList
)


label_widget = Label(app, text="copyPate App")

label_widget.pack()
lstbox_widget.pack()
button.pack()
button2.pack()
resetButton.pack()
time.sleep(.5)
app.mainloop()


