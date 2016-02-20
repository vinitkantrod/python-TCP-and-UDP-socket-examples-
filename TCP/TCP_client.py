import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 5000))

while 1:
	data = client_socket.recv(512)
	if(data == 'q' and data == 'Q'):
		client_socket.close()
		break
	else:
		print "Received :", data
		data = raw_input("Enter the text to send : ")
		if(data <> 'q' and data <> 'Q'):
			client_socket.send(data)
		else:
			client_socket.send(data)
			client_socket.close()
			break
