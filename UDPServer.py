import pickle
from socket import *

from share.ServerFunction import convert


def main():
    server_port = 13000

    with socket(AF_INET, SOCK_DGRAM) as SERVER_SOCKET:
        SERVER_SOCKET.bind(('', server_port))
        print ("The server is ready to receive")
        while True:
            message, client_address = SERVER_SOCKET.recvfrom(2048)
            print(f"packet [{message}] received from: {client_address}")
            modified_message = convert(pickle.loads(message))
            SERVER_SOCKET.sendto(pickle.dumps(modified_message), client_address)

if __name__ == "__main__":
    main()