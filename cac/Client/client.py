import socket
from cac.convertors import *


class Client:
    def __init__(self, host, port):
        self.address = (host, port)

    def send_command(self, command: str):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(self.address)
            sock.sendall(convert_to_bytes(command))
            received = convert_to_string(sock.recv(1024))
            return received
