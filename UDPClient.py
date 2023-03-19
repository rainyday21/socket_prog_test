from socket import *
import sys
serverName = input("Enter server name: ")
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
if (sys.argv[1]):
    file = open(sys.argv[1], "rb")
else:
    file=open(input('Input filename: '), "rb")
data = file.read(1024)
while (data):
    clientSocket.sendto(data,(serverName, serverPort))
    data = file.read(1024)
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
file.close()
clientSocket.close()
