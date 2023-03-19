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
	if not (isFile(message.decode())):
		option = message.decode()
	else:
		modifiedMessage = message.decode()
	if (option): 
		if (option = 'l'):
			
		elif (option = 'w'):
		
		elif (option = 'c'):

		else:
			modifiedMessage.append(0)
	serverSocket.sendto(modifiedMessage.encode(),clientAddress)	
