from pynput import keyboard


def on_activate():
    print('Global hotkey activated!')

def for_canonical(f):
    return lambda k: f(l.canonical(k))

paste = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+v'),
    on_activate)
copy = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+c'),
    on_activate)
    
with keyboard.Listener(
        on_press=for_canonical(copy.press),
        on_release=for_canonical(copy.release)) as l:
    l.join()
