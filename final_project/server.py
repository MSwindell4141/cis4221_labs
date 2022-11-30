import socket
import json
import os
import sys
import subprocess
import threading
import time

ip = '127.0.0.1'
port = 4141
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    socket.bind((ip, port))
except:
    print('Could not bind socket.')

socket.listen(1)

connection = socket.accept()
message = socket.recv(4096)
print(message)