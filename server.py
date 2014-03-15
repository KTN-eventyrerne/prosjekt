'''
KTN-project 2013 / 2014
Very simple server implementation that should serve as a basis
for implementing the chat server

'''

from clienthandler import ClientHandler
from threadedtcpserver import ThreadedTCPServer


if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 9999

    # Create the server, binding to localhost on port 9999
    server = ThreadedTCPServer((HOST, PORT), ClientHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
