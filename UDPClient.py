from socket import *
import sys
#serverName = input("Enter server name: ")
serverPort = 12000
if (sys.argv[3]):
    serverName = sys.argv[1]
    file = open(sys.argv[2], "rb")
    option = sys.argv[3]
elif (sys.argv[2]):
    serverName = sys.argv[1]
    file = open(sys.argv[2], "rb")
elif (sys.argv[1]):
    serverName = sys.argv[1]
    file = open(input('Enter filename'), "rb")
else:
    serverName = input('Enter server name: ')
    file = open(input('Enter filename'), "rb")
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
data = file.read(1024)
while (data):
    clientSocket.sendto(data,(serverName, serverPort))
    data = file.read(1024)
if (option):
    clientSocket.sendto(option.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
file.close()
clientSocket.close()