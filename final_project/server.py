import socket
import json
import os
import sys
import subprocess
import threading
import time

ip = '127.0.0.1'
port = 4141

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ip, port))
    s.listen()
    print("listening for connections...")
    conn, addr = s.accept()
    
    with conn:
        print(f"connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received {data!r}")
            conn.sendall(data)#can use this to send data back
print("server closed")