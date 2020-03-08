#!/usr/bin/python
# -*- coding: utf-8 -*-

from netmosquito_utils import *

buffer_size = 1     # How much data would you like to receive at once (bytes)
timeout_time = 2    # Timeout to avoid blocking


def parse_data(raw_data):
    '''Parses data. This function must be eddited by the user'''

    parsed_data = None
    '''
		The parsing Logic goes here, make shure to return parsed data
	'''
    return parsed_data


host, port = check_initial_params()
s = socket_setup(host, port, timeout_time)

while True:
    raw_data = receive_data(s, buffer_size)

    if not raw_data:
        # If no data is received, that means the connection has been closed
        # If you still want to keep receiving data, exclude this if (caution,
        # this may cause an infinite loop)
        print("\nConnection closed by server, exiting...")
        s.close()
        break
    parsed_data = parse_data(raw_data)

    '''
		The logic of the Challange after the parsing goes here
	'''

    try:
        send_data(s, parsed_data)
    except ConnectionResetError:
        print("\nConnection closed by server, exiting...")
        s.close()
        break
    except Exception as error:
        print(f"\nAn error has occured '{error}'")
        s.close()
        break
