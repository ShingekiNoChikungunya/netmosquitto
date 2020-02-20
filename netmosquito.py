import socket, sys

if len(sys.argv)==3:
	host=sys.argv[1] 		#Host IP goes here
	port=int(sys.argv[2]) 	#Port Goes Here

else:
	print(('Error while running, please execute proggram as following:\npython netmosquito.py <host> <port>'))
	exit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
s.settimeout(5)				#Sets the timeout time

def receive_data(s):
	#This functions recieves data in 4 bytes chunks until '\n' or '\r' is received
	data=''
	try:
		#Prevents exception from timeouts
		data+=s.recv(1).decode()
	except socket.timeout:
		return data

	while data[-1]!='\n':
		try:
			#Prevents exception from timeouts
			data+=s.recv(1).decode()
		except socket.timeout:
			break

	print(data,end='')
	return data

def parse_data(raw_data):
	parsed_data=None
	#This function parses the data received
	'''
		The parsing Logic goes here, make shure to return parsed data
	'''
	return parsed_data

def send_data(s,response):
	#This function sends the response to the server
	if response:
		s.send(bytes(response,'utf-8'))

while True:
	raw_data = receive_data(s)
	parsed_data = parse_data(raw_data)
	'''
		The logic of the Challange after the parsing goes here
	'''
	try:
		send_data(s,parsed_data)
	except ConnectionResetError:
		print("Connection closed by server")
		break
	except Exception as error:
		print(f"An error has occured '{error}'")
		break
