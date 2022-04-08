import socket
import random
import time

UDP_IP = ""
UDP_PORT = 0
redTeam = []
greenTeam =[]
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# default ("127.0.0.1", 7501, redteam array from program, greenteam array from program)
def initializeTester(ip, port, red, green):
    global sock
    global redTeam
    global greenTeam
    global UDP_IP
    global UDP_PORT
    UDP_IP = ip
    UDP_PORT = port
    redTeam = red
    greenTeam = green

def generateInteraction():  # sends a random interaction to the udp port
    if(len(redTeam) > 0 or len(greenTeam) > 0):
        redPlayer = redTeam[random.randint(0, len(redTeam)) - 1 ]
        greenPlayer = greenTeam[random.randint(0, len(greenTeam)) - 1]
        redHitsGreen = random.randint(0, 1) # 1 if red hits green, 0 if green hits red
        if(redHitsGreen == 1):
            message = "Red player " + redPlayer + " hit green player " + greenPlayer + "!"
            message = message.encode()
            sock.sendto(message, (UDP_IP, UDP_PORT))
        else:
            message = "Green player " + greenPlayer + " hit red player " + redPlayer + "!"
            message = message.encode()
            sock.sendto(message, (UDP_IP, UDP_PORT))
    else:
        sock.sendto("At least one team is empty, can't generate interaction", (UDP_IP, UDP_PORT))

