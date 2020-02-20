import socket, sys

buffer_size = 1				#How much data would you like to receive at once (bytes)
timeout_time= 2				#Timeout to not keep holding forever in case of incomplete packet

if len(sys.argv)==3:
	host=sys.argv[1] 		#Host IP goes here
	port=int(sys.argv[2]) 	#Port Goes Here

else:
	print(('Error while running, please execute proggram as following:\npython netmosquito.py <host> <port>'))
	exit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
print(f'Connection established with {host}:{str(port)}\n')
s.settimeout(timeout_time)	#Sets the timeout time

def receive_data(s):
	#This functions recieves data in n bytes chunks until '\n' is received or timeout ocurrs
	data=''
	try:					#Prevents exception from timeouts
		data+=s.recv(buffer_size).decode()
	except socket.timeout:
		return data

	while data[-1]!='\n':
		try:					#Prevents exception from timeouts
			data+=s.recv(buffer_size).decode()
		except socket.timeout:
			break

	if data != '\n':
		print(f'Received data:\n{data}')
	return data

def parse_data(raw_data):
	#This function parses the data received
	parsed_data=None
	'''
		The parsing Logic goes here, make shure to return parsed data
	'''
	return parsed_data

def send_data(s,response):
	#This function sends the response to the server
	if response:
		print(f'Sending data:\n{response}')
		s.send(bytes(response+'\n','utf-8'))

while True:
	raw_data = receive_data(s)
	if not raw_data:
		print("\nConnection closed by server, exiting...")
		s.close()
		break
	parsed_data = parse_data(raw_data)
	'''
		The logic of the Challange after the parsing goes here
	'''
	try:
		send_data(s,parsed_data)
	except ConnectionResetError:
		print("\nConnection closed by server, exiting...")
		break
	except Exception as error:
		print(f"\nAn error has occured '{error}'")
		break
