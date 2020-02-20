import socket, sys

try:
	host=sys.argv[1] 		#Host IP goes here
	port=int(sys.argv[2]) 	#Port Goes Here

except:
	print("Please inform host and port uppon executing")
	exit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

def receive_data(s):
	#This functions recieves data in 2048bytes chunks until '\n' is received
	data=''
	while True:
		data+=s.recv(2048).decode()
		if data[-1]=='\n':
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