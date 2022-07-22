import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234 ))
format = "utf-8"

while True:
    msg = s.recv(100)
    msg = msg.decode(format)
    print(msg)