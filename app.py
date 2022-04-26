import tkinter
from tkinter import font
from tkinter.constants import CENTER, END, FIRST, INSERT, LEFT, NONE, RAISED, RIGHT, SINGLE, TOP
from tkinter import Button, Label, Message, Radiobutton, Scrollbar, StringVar, Text, Listbox
import time
from typing import Counter
from pynput import keyboard
import pyperclip
import threading


lst = list(set())

app = tkinter.Tk()
app.title("copyPaste")
app.geometry("500x500")

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
      h.join()

def endProgram():
    global thread
    try:
        app.destroy()
        keyboard.Listener.stop
        thread.stop()
        thread_2.stop()
    except AttributeError:
        pass
    exit()

def make_clipboard():
    time.sleep(.02)
    blank = ""
    clipboard = app.clipboard_get()
    lst.append(clipboard)
    lstbox_widget.delete(0,END)
    for entry in lst:
        lstbox_widget.insert(END, entry)
    print(lst)
    main()

def copyAll():
    for i in lst[:]:
        if len(i)<=0:
            lst.remove(i)
    copied = "\n".join(lst)
    pyperclip.copy(copied)

def delete():
    threading.Thread()
    selection = lstbox_widget.get(lstbox_widget.curselection())              #Look up how to get the index of a certain selection then use in delete function.
    num = lst.index(selection)
    lstbox_widget.delete(num)

lstbox_widget = Listbox(
    app,
    justify=LEFT,
    selectmode=SINGLE,
    activestyle='none',
    width=50,
    height=20,
    font= "Arial 10"
)

delete_btn = Button(
    app,
    justify=CENTER,
    text="Delete Selection",
    command=delete

)
num_listbox = Listbox(
    app,
    justify=LEFT,
    selectmode=NONE,
    width=1,
    height=20,
    font="Arial 20"
)
def startFunc():
    global thread, thread_2
    thread = threading.Thread(target=main)
    thread.setDaemon(True)
    thread.start()
    thread_2 = threading.Thread(target=make_clipboard)
    thread_2.setDaemon(True)
    thread_2.start()
def resetList():
    lstbox_widget.delete(0,END)
    global lst
    lst.clear()


resetButton = Button(
    app,
    justify=CENTER,
    text="Reset List",
    command=resetList
)

copyAllButton = Button(
    app,
    justify=CENTER,
    text="Copy All",
    command=copyAll

)

setPasteButton = Button(
    app,
    justify=CENTER,
    text="Use Selection to Paste",
    command=selectPaste
)


label_widget = Label(app,
    text="The copyPaste App",
    font="Arial 18 bold"
 )
label_widget_name = Label(app,
    text="Developed By Owen Hankinson",
    font="Arial 8 italic"
 )

scrollBar = Scrollbar(app)
lstbox_widget.config(yscrollcommand = scrollBar.set)
scrollBar.config(command = lstbox_widget.yview) 

if __name__ == "__main__":
    label_widget.pack()
    label_widget_name.pack()
    lstbox_widget.pack()
    copyAllButton.pack()
    delete_btn.pack()
    setPasteButton.pack()
    resetButton.pack()
    app.after_idle(startFunc)
    time.sleep(.5)
    app.protocol("WM_DELETE_WINDOW", endProgram)
    app.mainloop()
 