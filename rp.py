LISTEN_PORT = 8001
SERVER_PORT = 9001
SERVER_ADDR = "localhost"
 
from twisted.internet import protocol, reactor
 

class ServerProtocol(protocol.Protocol):
    def __init__(self):
        self.buffer = None
        self.client = None
 
    def connectionMade(self):
        factory = protocol.ClientFactory()
        factory.protocol = ClientProtocol
        factory.server = self
 
        reactor.connectTCP(SERVER_ADDR, SERVER_PORT, factory)
 
    # Client =&amp;amp;gt; Proxy
    def dataReceived(self, data):
        if self.client:
            self.client.write(data)
        else:
            self.buffer = data
 
    # Proxy =&amp;amp;gt; Client
    def write(self, data):
        self.transport.write(data)
 
class ClientProtocol(protocol.Protocol):
    def connectionMade(self):
        self.factory.server.client = self
        self.write(self.factory.server.buffer)
        self.factory.server.buffer = ''
 
    # Server =&amp;amp;gt; Proxy
    def dataReceived(self, data):
        self.factory.server.write(data)
 
    # Proxy =&amp;amp;gt; Server
    def write(self, data):
        if data:
            self.transport.write(data)
 
def main():
    factory = protocol.ServerFactory()
    factory.protocol = ServerProtocol
 
    reactor.listenTCP(LISTEN_PORT, factory)
    reactor.run()
 
if __name__ == '__main__':
    main()