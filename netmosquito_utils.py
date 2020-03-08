import socket
import sys


def check_initial_params():
    '''Cheks if host and port where assigned then return them'''
    if len(sys.argv) == 3:
        host = sys.argv[1]
        port = int(sys.argv[2])

    else:
        print('Error while running, please use as following:\npython netmosquito.py <host> <port>')
        exit()

    return host, port


def socket_setup(host, port, timeout_time=None):
    '''Setup the socket that will be used'''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print(f'Connection established with {host}:{str(port)}\n')
    sock.settimeout(timeout_time)
    return sock


def receive_data(sock, buffer_size=2048):
    '''Receives data in n bytes until "\n" is received'''
    received_data = ''
    data = ''

    while received_data != '\n':
        try:
            received_data = sock.recv(buffer_size).decode()
            data += received_data
        except socket.timeout:
            break

    if data != '\n':
        print(f'Received data:\n{data}')
    return data


def send_data(sock, response):
    '''Sends the response to the server if not Nulll'''
    if response:
        print(f'Sending data:\n{response}')
        sock.send(bytes(response + '\n', 'utf-8'))
