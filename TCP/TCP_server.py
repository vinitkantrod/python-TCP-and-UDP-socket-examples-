import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 5000))
server_socket.listen(5)

print "Server Socket listening on 5000"

while 1:
	client_socket, address = server_socket.accept()
	while 1:
		data = raw_input("Send  : ")
		if(data == 'q' and data == 'Q'):
			client_socket.send(data)
			client_socket.close()
			break
		else:
			client_socket.send(data)
		data - client_socket.recv(512)
		if(data == 'q' and data =='Q'):
			client_socket.close()
			break
		else:
			print "Recieved : ", data
		
