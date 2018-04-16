from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)
tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print("等待链接")
    tcpCliSock,addr = tcpSerSock.accept();
    print("从",addr,"发起的请求");

    while True:
        data = tcpCliSock.recv(BUFSIZ).decode()
        if not data:
            break
        print("data= ",data)
        tcpCliSock.send(('[%s] %s' %(ctime(),data)).encode())
    tcpCliSock.close()
tcpSerSock.close()