import pyperclip
from app import lstbox_widget, lst
import time

def defaultAction():
    pos = 1
    if pos >= len(lst):
        pyperclip.copy("")
        print('No more Copies')
    else:
        pyperclip.copy(lst[pos])
        time.sleep(.01)
        pos += 1

def selectPaste():
    selection = lstbox_widget.get(lstbox_widget.curselection())
    pyperclip.copy(selection)