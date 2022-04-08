from doctest import IGNORE_EXCEPTION_DETAIL
import udpTester
import socket
import time

UDP_IP = ""
UDP_PORT = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# use initlizeSocket("127.0.0.1", 7051) unless something changes
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
    #    -This makes sure receiving multiple packets at once doesn't lose data
    data = []
    while True:
        try:
            data.append(sock.recvfrom(1024))
        except:
            break
    return data

# test code (run udp.py by itself with this if you need to verify that the connection)
#socketDetails = ["127.0.0.1", 7501]
#initlizeSocket(socketDetails[0], socketDetails[1])
#tester = udpTester
#udpTester.initializeTester(socketDetails[0], socketDetails[1], ["rick", "bob"], ["tony", "jim"])
#while(True):
#    time.sleep(1)
#    udpTester.generateInteraction()
#    udpTester.generateInteraction()
#    data = getData()
#    for x in data:
#        print(x[0].decode())
