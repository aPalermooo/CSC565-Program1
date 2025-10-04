import pickle

from share.ClientFunction import *


def main():

    serverPort = 13000

    with socket(AF_INET, SOCK_STREAM) as client_socket:
        message = create_message("TCP")
        client_socket.connect((message.destination, serverPort))
        client_socket.send(pickle.dumps(message))
        modified_message = client_socket.recv(2048)
        if modified_message is None:
            exit(-1)
        return_message(message, pickle.loads(modified_message))


if __name__ == "__main__":
    main()