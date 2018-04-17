from twisted.internet import protocol , reactor
from time import ctime

PORT = 21567

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print("...watting connection...")
    def dataReceived(self,data):
        self.transport.write('[%s] %s' % (ctime(),data))

factory = protocol.Factory()
factory.protocol = TSServProtocol
print("...watting connection...")
reactor.listenTcp(PORT,factory)
reactor.run()