from tkinter.constants import CENTER, END, FIRST, INSERT, LEFT, RAISED, RIGHT, SINGLE, TOP
from tkinter import Button, Label, Message, Radiobutton, Scrollbar, StringVar, Text, Listbox
import tkinter
import time
from typing import Counter
from pynput import keyboard
import pyperclip
import threading
import _thread


lst = list(set())

app = tkinter.Tk()
app.title("copyPaste")
app.geometry("500x300")

def selectPaste():
    global lst
    if len(lst) > 0:
        selection = lstbox_widget.get(lstbox_widget.curselection())
        pyperclip.copy(selection)
    else:
        pass

def main():
    with keyboard.GlobalHotKeys({
    '<ctrl>+c': make_clipboard,
    '<ctrl>+<shift>+r': endProgram,}) as h:
        try:
            h.join()
        except Exception:
            print("Thread Listener could not start")
            exit()

def endProgram():
    return print("Done")

def make_clipboard():
    time.sleep(.1)
    clipboard = app.clipboard_get()
    lst.append(clipboard)
    lstbox_widget.delete(0,END)
    for entry in lst:
        lstbox_widget.insert(END, entry)
    print(lst)
    main()

def appendSelectButton():
    setPasteButton.pack()
    threading.Thread(target=main).start()
lstbox_widget = Listbox(
    app,
    justify=LEFT,
    selectmode=SINGLE,
    activestyle='none',
    width=50,
    height=20

)

default_section = Radiobutton(
    app,
    text= "More Modes availible soon",
    command=None
)

select_mode = Radiobutton(
    app,
    text= "Select Mode",
    command=appendSelectButton
)
def resetList():
    lstbox_widget.delete(0,END)
    global lst
    lst.clear()


resetButton = Button(
    app,
    justify=RIGHT,
    text="Reset List",
    command=resetList
)


setPasteButton = Button(
    app,
    justify=CENTER,
    text="Use Selection to Paste",
    command=selectPaste
)


label_widget = Label(app, text="copyPate App")


if __name__ == "__main__":
    label_widget.pack()
    lstbox_widget.pack()
    resetButton.pack()
    select_mode.pack()
    default_section.pack()
    time.sleep(.5)
    app.mainloop()
