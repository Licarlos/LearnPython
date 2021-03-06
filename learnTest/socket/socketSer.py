from socketserver import (TCPServer as TCP,StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST,PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print("...connected from:",self.client_address)
        self.wfile.write(('[%s] %s' % (ctime(),self.rfile.readline())).encode())

tcpServ = TCP(ADDR,MyRequestHandler)
print("...watting connecting...")
tcpServ.serve_forever()