from server import run_tcp_server

if __name__ == "__main__":
    HOST, PORT = "10.0.0.72", 9999
    run_tcp_server(HOST, PORT)
