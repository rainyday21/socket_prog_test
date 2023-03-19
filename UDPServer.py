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
	if len(message.decode()) == 1:
		option = message.decode()
	else:
		modifiedMessage = message.decode()
	if (option):
		recFile.close()
		recFile = open("temp.txt", "rb") 
		if option == 'l':
			finalMessage = "Lines: " + str(len(recFile.read())) + "\n" + modifiedMessage
		elif (option == 'w'):
			finalMessage = "Words: " + str(len((recFile.read()).split(' '))) + '\n' + modifiedMessage
		elif (option == 'c'):
			finalMessage = "Characters: " + str(len(recFile.read())) + '\n' + modifiedMessage
		else:
			finalMessage = modifiedMessage
	serverSocket.sendto(finalMessage.encode(),clientAddress)	
