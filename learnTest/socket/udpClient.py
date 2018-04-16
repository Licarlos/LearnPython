from socket import *

HOST = 'localhost'
PORT = 21567
ADDR = (HOST,PORT)
BUFSIZ = 1024

udpCliSock = socket(AF_INET,SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    udpCliSock.sendto(data.encode(),ADDR)
    data,addr = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data.decode())
udpCliSock.close()