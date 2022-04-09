from doctest import IGNORE_EXCEPTION_DETAIL
import udpTester
import socket
import time

class udpsocket:
    def __init__(self) -> None:
        self.UDP_IP = "127.0.0.1"
        self.UDP_PORT = 7051
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    # use initlizeSocket("127.0.0.1", 7051) unless something changes
    def initlizeSocket(self):  

        self.sock.bind((self.UDP_IP, self.UDP_PORT))
        self.sock.settimeout(.1)

    def getData(self):
        # will keep loading data into the data array until there isn't anymore being received for 100 ms, then returns the array
        #    -This makes sure receiving multiple packets at once doesn't lose data
        data = []
        while True:
            try:
                data.append(self.sock.recvfrom(1024))
            except:
                break
        return data

    #RUNS THE SOCKET PROGRAM, INCLUDES ABOVE FUNCTIONS
    def runSocket(self, team1, team2):

        self.initlizeSocket()
        udpTester.initializeTester(self.UDP_IP, self.UDP_PORT, team1, team2)
        while(True):
            time.sleep(1)
            udpTester.generateInteraction()
            udpTester.generateInteraction()
            data = self.getData()
            for x in data:
                print(x[0].decode())


#test the program: to run, uncomment below and in console "python3 udp.py"
# newSocket = udpsocket()
# newSocket.runSocket(["rick", "bob"], ["tony", "jim"])
