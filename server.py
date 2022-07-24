import socket
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
format = "utf-8"
HeaderSize = 10
connlist = []


class Client(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn

    def run(self):
        handle_client(self.conn)


def handle_client(conn):
    global format
    global HeaderSize
    while True:
        msg = conn.recv(HeaderSize)
        if len(msg):
            msg_length = int(msg[:HeaderSize])
            msg += conn.recv(msg_length)
            print(msg.decode())
            msg = msg.decode()
            for i in connlist:
                if i != conn:
                    i.send(bytes(msg, format))


def recv_clients():
    s.listen()
    while True:
        conn, addr = s.accept()
        connlist.append(conn)
        thread = Client(conn)
        thread.start()


recv_clients()