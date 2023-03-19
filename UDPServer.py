from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
count=0
while True:
	message, clientAddress = serverSocket.recvfrom(1024)
	modifiedMessage = message.decode()
	count+=1
	print(count)
	serverSocket.sendto(modifiedMessage.encode(),clientAddress)	