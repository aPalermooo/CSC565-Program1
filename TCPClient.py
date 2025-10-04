import pickle
import socket

from share.ClientFunc import create_message, return_message
from share.Message import Message


CLIENT_TIMEOUT_LENGTH = 5

def create_client(m : Message):

    serverPort = 13000
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as CLIENT_SOCKET:

            CLIENT_SOCKET.settimeout(CLIENT_TIMEOUT_LENGTH)

            try:
                CLIENT_SOCKET.connect((m.destination, serverPort))
                CLIENT_SOCKET.send(pickle.dumps(m))
                modified_message = CLIENT_SOCKET.recv(2048)
                if modified_message is None:
                    exit(-1)
                return_message(m, pickle.loads(modified_message))
                break
            except (socket.timeout, TimeoutError):
                print("Timed out")
                if input("Try again? (y/n) $").strip().lower() == "y":
                    continue
                else:
                    break
            except ConnectionRefusedError:
                print("Connection Refused: Check if server is open")
                if input("Try again? (y/n) $").strip().lower() == "y":
                    continue
                else:
                    break
                break

def main():
    while True:
        args = input("(env) $")

        args = args.strip().split(' ')

        if args[0] == "exit":
            exit(0)


        if args [0] != "Convert":
            print("unknown command\n")
            continue

        try:
            message = create_message("TCP", args[1:])
        except RuntimeError:
            continue

        create_client(message)

if __name__ == "__main__":
    main()