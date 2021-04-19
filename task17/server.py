import socket
from threading import Thread
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

serverip="ur server ip"
serverport=1234
ip="ur client ip"
port=10048
s.bind( (serverip,serverport) )
print("welcome to chat server".center(60))

def recv():

    while True:
        x=s.recvfrom(1024)
        data=x[0].decode()
        print("\nreceived>> "+data)
        if data == "bye":
            exit()

def send():
    while True:
        string=input("send>> ")
        s.sendto(bytes(string.encode()),(ip,port))

        if string == "bye":
            exit()

Thread(target=recv).start()
Thread(target=send).start()
