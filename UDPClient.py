from socket import *

# TODO:
# THREAD

def main():
    server_name = 'localhost'
    server_port = 13000

    with socket(AF_INET, SOCK_DGRAM) as CLIENT_SOCKET:

        if CLIENT_SOCKET is None:
            print("FAILED TO OPEN SOCKET")

        message = input('Input lowercase sentence:')
        CLIENT_SOCKET.sendto(message.encode(),
                                    (server_name, server_port))
        modified_message, server_address = \
                                    CLIENT_SOCKET.recvfrom(2048)
        print(modified_message.decode())
        CLIENT_SOCKET.close()

if __name__ == "__main__":
    main()