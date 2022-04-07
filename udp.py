import socket
import time

UDP_IP = ""
UDP_PORT = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def initlizeSocket(IP, PORT):
    global UDP_IP     # global keywords grabs the global variables instead of re-declaring them in the function
    global UDP_PORT
    global sock
    UDP_IP = IP 
    UDP_PORT = PORT
    sock.bind((UDP_IP, UDP_PORT))
    sock.settimeout(.1)

def getData():
    # will keep loading data into the data array until there isn't anymore being received for 100 ms, then returns the array
    data = []
    while True:
        try:
            data.append(sock.recvfrom(1024))
        except:
            break
    return data
