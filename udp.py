from doctest import IGNORE_EXCEPTION_DETAIL
import udpTester
import socket
import time

# data = ""

class udpsocket:

    def __init__(self) -> None:
    # def__init__(self):
        self.UDP_IP = "127.0.0.1"
        self.UDP_PORT = 7051
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.data = []
        self.cleandata = []
        
    # use initlizeSocket("127.0.0.1", 7051) unless something changes
    def initlizeSocket(self):  
        print(self.UDP_IP)
        print(self.UDP_PORT)
        self.sock.bind((self.UDP_IP, self.UDP_PORT))
        self.sock.settimeout(.1)

    def getData(self):
        # will keep loading data into the data array until there isn't anymore being received for 100 ms, then returns the array
        #    -This makes sure receiving multiple packets at once doesn't lose data
        while True:
            try:
                self.data.append(self.sock.recvfrom(1024))
            except:
                break
        #Decodes data in self.data once retrieved from socket
        for x in self.data:
            if x[0].decode() not in self.cleandata:
                self.cleandata.append(x[0].decode())

    #RUNS THE SOCKET PROGRAM, INCLUDES ABOVE FUNCTIONS
    def runSocket(self):
        udpTester.initializeTester(self.UDP_IP, self.UDP_PORT, self.red, self.green)
        time.sleep(1)
        udpTester.generateInteraction()
        udpTester.generateInteraction()
        self.getData()
        for x in self.cleandata:
            print(x)
        

    def getTeam(self, redTeam, greenTeam):
        self.red = redTeam
        self.green = greenTeam
        print(self.red)
        print(self.green)
