import socket
import sys, signal
import json

def signal_handler(signal, frame):
    print("\nExist")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# print("Enter host: ")
# HOST = str(input())  # The server's hostname or IP address
HOST = "127.0.0.1"

print("Enter port: ")
PORT = int(input())

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        msg = str(input())    
        s.sendto(msg.encode(), (HOST, PORT))
        data = s.recv(1024)
        string = data.decode('utf-8')
        json_obj = json.loads(data)
        print(f"JSON: {json_obj}")
except KeyboardInterrupt:
    print("Interrupted")