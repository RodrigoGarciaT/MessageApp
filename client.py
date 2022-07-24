import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((socket.gethostname(), 1234))
format = "utf-8"

while True:
    msg = input(">you ")
    server.send(bytes(msg, format))
    msg = server.recv(1024)
    msg = msg.decode()
    print(msg)
