import socket
import threading
client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 1234))
format = "utf-8"
HeaderSize = 10
msg_list = []


def get_msgs():
    global format
    global HeaderSize
    full_msg = ''
    new_msg = True
    msg_length = 0
    while True:
        msg = client_socket.recv(HeaderSize)
        if new_msg:
            msg_length = int(msg[:HeaderSize])
            new_msg = False

        full_msg += msg.decode(format)

        if len(full_msg) - HeaderSize == msg_length:
            msg_list.append(full_msg[HeaderSize:])
            full_msg = ''
            new_msg = True


def main():
    global format
    global HeaderSize
    while True:
        msg = input(">you ")
        msg = msg.encode(format)
        msg_length = len(msg)
        msg_length = str(msg_length).encode(format)
        msg_length += b' '*(HeaderSize- len(msg_length))
        client_socket.send(msg_length)
        client_socket.send(msg)

        for i in msg_list:
            print(i)
            msg_list.remove(i)


x= threading.Thread(target = main)
y= threading.Thread(target = get_msgs)
x.start()
y.start()
x.join()
y.join()