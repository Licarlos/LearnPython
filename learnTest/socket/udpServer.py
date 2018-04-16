from socket import *
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST,PORT)
BUFSIZ = 1024

udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print("...watting connection...")
    data,addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto(("[%s] %s" % (ctime,data)).encode(),addr)
    print("连接来自",addr)
udpSerSock.close()