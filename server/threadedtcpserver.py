import SocketServer
from clienthandler import ClientHandler
from threadedtcpserver import ThreadedTCPServer

'''
This will make all Request handlers being called in its own thread.
Very important, otherwise only one client will be served at a time
'''

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    self.clients = {}
    self.messages = []
    SocketServer.TCPServer.__init__(self,hostPort,clientHandler)
	
	
if __name__ == "__main__":
    HOST = 'localhost'

    PORT = 9999

    # Create the server, binding to localhost on port 9999
    server = ThreadedTCPServer((HOST, PORT), ClientHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()