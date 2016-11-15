#socket progrmaming 
import sys
import socket


server = 'localhost'   
port = 5777

#AF_INET is the socket_family and SOCK_STREAM is socket_type indicating it's connection orineted
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print(s)
#Get local machine name
server_ip = socket.gethostbyname(server) 
print(server_ip)
#bind ip address to the port
s.bind((server_ip,port))

#queue up to 5 request 
s.listen(5)

while True:
	#establish a connection
	clientSocket, addr = s.accept()
	request = clientSocket.recv(1024)
	req = request.decode("utf-8").split('\n')[0].split(' ')[1]
	print(req.split('/')[1])

	print('Got a connection from %s' % str(addr))
	print(clientSocket)

	fd = open('index.html','r')
	msg = fd.read()
	fd.close()
	
	#encode the message to send in UTF-8
	clientSocket.send(msg.encode('utf-8'))

	#close the socket
	clientSocket.close()

