import pickle
from socket import *

from share.ServerFunction import convert


def main():

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
    main()