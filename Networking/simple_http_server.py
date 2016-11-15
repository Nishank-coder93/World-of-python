#http-server
import sys
import socket

#command line argumnets 
#checks if the correct number of argument is being entered 
if len(sys.argv) != 2:
	print('Usage : python3 <filename> <port-number>')
	exit()
else:
	port = int(sys.argv[1])

server_addr = 'localhost'
socket_type = socket.SOCK_STREAM #connection oriented 
socket_family = socket.AF_INET  #ipv4 version INET 

#getting the local machine ip address in this case it's localhost
server_ip = socket.gethostbyname(server_addr)
print('Started server at %s:%s' % (server_ip,str(port)))
#creating a socket descriptor 
sock = socket.socket(socket_family,socket_type)

#bind the ip address and port to socket
sock.bind((server_ip,port))

#listen upto 5 request
sock.listen(5)

while True:
	#establish a connection
	clientSocket,client_addr = sock.accept()
	print(client_addr,"Client made a request")

	#receive only 1024 bytes of request from the client
	req = clientSocket.recv(1024)

	#filter the incoming request for information and file request
	requested_info = req.decode('utf-8').split('\n')
	#TODO with requested info
	file_requested = requested_info[0].split(' ')
	file_requested = file_requested[1].split('/')
	if len(file_requested) > 1:
		file_requested = file_requested[1]
		print("%s file requested by client " % file_requested)
	else:
		pass

	#open file requested by the client
	try:
		with open(file_requested,'r') as file_handler:
			msg = file_handler.read()
			file_handler.close()

			#encode the message to send in utf-8

			clientSocket.send(msg.encode('utf-8'))
			clientSocket.close()
			
	#exception if the file doesnt exist 		
	except IOError as e:
		print('Unable to open file : %s' % str(e))
		error_msg = '<h1 style="width:100%; align-text:center;"> 404 ERROR: file Requested not found or has been deleted </h1>'
		clientSocket.send(error_msg.encode(('utf-8')))
		clientSocket.close()

sock.close()