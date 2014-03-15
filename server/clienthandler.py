import SocketServer

'''
The RequestHandler class for our server.

It is instantiated once per connection to the server, and must
override the handle() method to implement communication to the
client.
'''

class ClientHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        # Get a reference to the socket object
        self.connection = self.request
        # Get the remote ip adress of the socket
        self.ip = self.client_address[0]
        # Get the remote port number of the socket
        self.port = self.client_address[1]
        print 'Client connected @' + self.ip + ':' + str(self.port)
        # Wait for data from the client
        data = self.connection.recv(1024).strip()
        # Check if the data exists
        # (recv could have returned due to a disconnect)
        if data:
            print data
            # Return the string in uppercase
            self.connection.sendall(data.upper())
        else:
            print 'Client disconnected!'
