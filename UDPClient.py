import pickle
import socket

from share.ClientFunc import create_message, return_message
from share.Message import Message


# TODO:
# THREAD

def create_client(m : Message):
    server_port = 13000

    while True:
        print("Opening Socket...")
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as CLIENT_SOCKET:

            CLIENT_SOCKET.settimeout(5)
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