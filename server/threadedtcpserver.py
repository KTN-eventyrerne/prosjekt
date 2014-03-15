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
	
	def add_client(self, nickname, ClientHandler):
		if not self.list.has_key(username)
			self.clients[nickname]=ClientHandler

    def send_to_all(self, msg_raw):
        msg = username + " said @" + time.strftime("%H:%M") + ": " + msg_raw
        self.messages.append(msg)
        for clienthandler in self.list.itervalues():
            clienthandler.send_to_client(msg)
	
    def remove_client(self, username):
		if self.clients.has_key(username):
			self.list.pop(username,None)
		
    def get_messages(self):
        return self.messages
	
	
if __name__ == "__main__":
    HOST = 'localhost'

    PORT = 9999

    # Create the server, binding to localhost on port 9999
    server = ThreadedTCPServer((HOST, PORT), ClientHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()