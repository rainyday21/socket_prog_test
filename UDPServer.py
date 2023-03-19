from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
count=0
recFile = open("temp.txt", "wb")
message, clientAddress = serverSocket.recvfrom(1024)
while True:
	#modifiedMessage = message.decode()
	recFile.write(message)
	serverSocket.settimeout(3)
	message, clientAddress = serverSocket.recvfrom(1024)

recFile.close()
serverSocket.sendto(modifiedMessage.encode(),clientAddress)	