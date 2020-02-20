import socket, sys

if len(sys.argv)==3:
	host=sys.argv[1] 		#Host IP goes here
	port=int(sys.argv[2]) 	#Port Goes Here

else:
	print(('Error while running, please execute proggram as following:\npython netmosquito.py <host> <port>'))
	exit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
s.settimeout(1)				#Sets the timeout time

def receive_data(s,data=''):
	#This functions recieves data in 2048bytes chunks until '\n' is received
	try:
		#Prevents exception from timeouts
		data+=s.recv(2048).decode()
	except:
		return data
	while data[-1]!='\n' or data[-1]!='\r':
		try:
			#Prevents exception from timeouts
			data+=s.recv(2048).decode()
		except:
			break

	return data

def parse_data(raw_data):
	#This function parses the data received
	parsed_data='\n'
	'''
		The parsing Logic goes here
	'''
	return parsed_data

def send_data(s,parsed_data):
	#This function sends the response to the server
	s.send(bytes(parsed_data,'utf-8'))

while True:
	raw_data = receive_data(s)
	parsed_data = parse_data(raw_data)
	try:
		send_data(s,parsed_data)
	except ConnectionResetError:
		print("Connection closed by server")
		break
	except:
		print("An error has occured")
		break
