import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
format = "utf-8"


def recv_clients():
    while True:
        conn, addr = s.accept()
        conn.send(bytes("Hello man", format))
        print(conn)


recv_clients()