
import pyautogui as pya
import time
import keyboard as kb
from tkinter import Tk
import pyperclip

list = []


app = Tk()
app.title("copyPaste")
app.geometry("400x400")


def main():
    print("Copy Your Statements")
    while True:
        if kb.is_pressed('ctrl') == True and kb.is_pressed('c') == True:
            time.sleep(.2)
            print("Word Copied")
            make_clipboard()
        if kb.is_pressed('f10') == True:
            print("Start Pasting")
            time.sleep(1)
            pyperclip.copy(list[0])
            break

def make_clipboard():
    print("Appending to list")
    clipboard = app.clipboard_get()
    list.append(clipboard)
    print(list)

def runBack():
        pos = 0
        while True:
            if kb.is_pressed('ctrl') == True and kb.is_pressed('v') == True:

                if pos > len(list):
                    pyperclip.copy("")
                    break
                else:
                    pyperclip.copy(list[pos])
                    time.sleep(.3)
                    pos += 1
                
            if kb.is_pressed('f10') == True:
                print("Ending Program")
                break
