import socket
import json
import os
import sys
import subprocess
import threading
import time

print('Backdoor starting')
ip = '127.0.0.1'
port = 4141
socket = socket.socket()
try:
    socket.connect((ip, port))
    socket.send('This is a message from the backdoor')
except:
    print('nope')
