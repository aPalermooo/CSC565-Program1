import pickle
from socket import *

from share.ClientFunction import create_message, return_message


# TODO:
# THREAD

def main():
    server_port = 13000

    with socket(AF_INET, SOCK_DGRAM) as CLIENT_SOCKET:

        if CLIENT_SOCKET is None:
            print("FAILED TO OPEN SOCKET")

        message = create_message("UDP")
        CLIENT_SOCKET.sendto(pickle.dumps(message), (message.destination, server_port))
        modified_message, server_address = CLIENT_SOCKET.recvfrom(2048)
        return_message(message, pickle.loads(modified_message))

if __name__ == "__main__":
    main()