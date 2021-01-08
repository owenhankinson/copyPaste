import keyboard as kb
import time
import pyperclip
import threading
from pynput import keyboard
from app import lstbox_widget
from key_listner import for_canonical
from paste_gui import pastingFunction



def main():
    with keyboard.Listener(
        on_press=for_canonical(copy.press),
        on_release=for_canonical(copy.release)) as l:
        l.join()
    with keyboard.Listener(
        on_press=for_canonical(paste.press),
        on_release=for_canonical(paste.release)) as thread:
        thread.join()

    
paste = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+v'),
    pastingFunction)

copy = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+c'),
    make_clipboard)
