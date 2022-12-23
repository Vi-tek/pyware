import socketserver
from cac.convertors import *
from cac.Server.server_terminal import server_terminal


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()
        print(f"{self.client_address} wrote: {data}")
        rv = server_terminal.run_command(convert_to_string(data), False)
        print(f"sending packet back: {rv}")
        self.request.sendall(convert_to_bytes(rv))


def run_tcp_server(host, port):
    with socketserver.TCPServer((host, port), TCPHandler) as server:
        server.serve_forever()
