###################################
# Name:         UDPClient.py
# Description:  Implementation of a UDP client.
#               Client is responsible for prompting user for commands, sending data to server, and relaying data from server to user
#
# Author: Xander Palermo <ajp2s@missouristate.edu>
# Class: CSC565 - Computer Networking
# Assignment: Socket Programming Assignment 1
####################################

import pickle
import socket

from share.ClientFunction import create_message, return_message
from share.Message import Message



CLIENT_TIMEOUT_LENGTH = 5

def create_client(m : Message):
    """
    Creates a query to a server and logs its reply in terminal.
        Uses a UDP connection
    :param m: Message containing all information regarding the query
    :return: None
    """
    server_port = 13000

    while True:
        print("Opening Socket...")
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as CLIENT_SOCKET:

            CLIENT_SOCKET.settimeout(CLIENT_TIMEOUT_LENGTH)
            try:
                CLIENT_SOCKET.sendto(pickle.dumps(m), (m.destination, server_port))
                modified_message, server_address = CLIENT_SOCKET.recvfrom(2048)
                print("Response Received")
                return_message(m, pickle.loads(modified_message))
                break
            except (socket.timeout, TimeoutError):
                print("Timed out")
                if input("Try again? (y/n) $").strip().lower() == "y":
                    continue
                else:
                    break


def main():
    """
    A custom shell used to form queries directed to a server
    :return: exit(0)
    """
    while True:
        args = input("(env) $")

        args = args.strip().split(' ')

        if args[0] == "exit":
            exit(0)


        if args [0] != "Convert":
            print("unknown command\n")
            continue

        try:
            message = create_message("UDP", args[1:])
        except RuntimeError:
            continue

        create_client(message)

if __name__ == "__main__":
    main()