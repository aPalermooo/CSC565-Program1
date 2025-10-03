from socket import *


def main():
    server_port = 12000

    with socket(AF_INET, SOCK_DGRAM) as SERVER_SOCKET:
        SERVER_SOCKET.bind(('', server_port))
        print ("The server is ready to receive")
        while True:
            message, client_address = SERVER_SOCKET.recvfrom(2048)
            modified_message = message.decode().upper()
            SERVER_SOCKET.sendto(modified_message.encode(),\
                                                            client_address)

if __name__ == "__main__":
    main()