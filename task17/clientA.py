import socket
from threading import Thread
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

serverip="192.168.0.105"
serverport=1234
ip="192.168.0.104"
port=10048
s.bind( (ip,port) )
print("welcome to chat server".center(60))

def send():
    while True:
        string=input("send>> ")
        s.sendto(bytes(string.encode()),(serverip,serverport))
        if string == "bye":
            exit()

def recv():
    while True:
        x=s.recvfrom(1024)
        data=x[0].decode()
        print("\nreceived>> "+data)
        if data == "bye":
            exit()


Thread(target=send).start()

Thread(target=recv).start()