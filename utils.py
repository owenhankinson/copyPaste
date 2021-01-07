import keyboard as kb
import time
import pyperclip
import threading
from app import make_clipboard
threading.Thread(target=lambda:[main(), runBack()])

lst = []

def main():
    x = 5
    while True:
        if kb.is_pressed('ctrl') == True and kb.is_pressed('c') == True:
            time.sleep(.2)
            print("Word Copied")
            make_clipboard()
        if kb.is_pressed('f10') == True:
            print("Start Pasting")
            time.sleep(1)
            pyperclip.copy(lst[0]) 
            break

def runBack():
    global lst
    pos = 0
    while True:
        if lst == []:
            return print("No Items have been copied")
        if kb.is_pressed('ctrl') == True and kb.is_pressed('v') == True:

            if pos >= len(lst):
                pyperclip.copy("")
                print('No more Copies')
                break
            else:
                pyperclip.copy(lst[pos])
                time.sleep(.01)
                pos += 1
        if kb.is_pressed('f10') == True:
            print("Ending Program")
            break

