import socket

client = socket.socket()

while(True):
    host = raw_input("Friend's IP (127.0.0.1 if local): ")

    try:
        port = int(raw_input("Friend's port (12345 if they choose default: "))
        break
    except:
        print("Invalid port provided")

