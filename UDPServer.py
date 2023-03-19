from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
count=0
while True:
	message, clientAddress = serverSocket.recvfrom(1024)
	modifiedMessage = message.decode().lower()
	lines = "Lines: " + message.decode().count('\n') + '\n'
	words = "Words: " + str(len(message.decode().split(' '))) + '\n'
	char = "Characters: " + str(len(message.decode())/4) + '\n'
	finalMessage = lines + words + char + modifiedMessage
	serverSocket.sendto(finalMessage.encode(),clientAddress)
	serverSocket.timeout(2)	