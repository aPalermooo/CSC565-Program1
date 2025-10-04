###################################
# Name:         TCPServer.py
# Description:  Implementation of a TCP server.
#               Server is responsible for accepting data from clients, performing conversions on data (as requested), and returning data
#
# Author: Xander Palermo <ajp2s@missouristate.edu>
# Class: CSC565 - Computer Networking
# Assignment: Socket Programming Assignment 1
####################################

import pickle
from socket import *

from share.ServerFunction import convert


def main():
    """
    A server that remains active listening on port 13000
        Uses TCP connection
    :return: None
    """
    serverPort = 13000

    with socket(AF_INET, SOCK_STREAM) as server_socket:
        server_socket.bind(('', serverPort))
        server_socket.listen(1)
        print('The server is ready to receive')

        while True:
            connectionSocket, addr = server_socket.accept()
            message = pickle.loads(connectionSocket.recv(2048))
            print(f"packet [{message}] received from: {addr}")
            modified_message = convert(message)
            connectionSocket.send(pickle.dumps(modified_message))
            connectionSocket.close()

if __name__ == "__main__":
    #init server
    main()