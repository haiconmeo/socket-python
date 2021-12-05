from twisted.web import proxy
from twisted.internet import reactor,protocol
from twisted.python import log
import sys



class MyProxy(protocol.Protocol):
    def dataReceived(self, data):
        print("data",data)
        return  data




factory = protocol.ClientFactory()
factory.protocol = MyProxy
reactor.listenTCP(8081, factory)
reactor.run()