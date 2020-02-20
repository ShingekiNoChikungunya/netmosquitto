import socket

host='127.0.0.1' #Host IP goes here
port=7000		 #Port Goes Here

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(host,port)

def recieve_data(s):
	data = s.recv(2048)
	return data

def parse_data(raw_data):
	return response

def send_data(parsed_data):
	s.send(parsed_data)

while True:
	raw_data = recieve_data(s)
	parsed_data = parsed_data(raw_data)
	send_data(parsed_data)