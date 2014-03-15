'''
KTN-project 2013 / 2014
Very simple server implementation that should serve as a basis
for implementing the chat server

'''

import argparse

from clienthandler import ClientHandler
from threadedtcpserver import ThreadedTCPServer

parser = argparse.ArgumentParser()
parser.add_argument('host', help="Host address to listen on")
parser.add_argument('port', type=int, help="Port to listen on")
args = parser.parse_args()

if __name__ == "__main__":
    # Create the server, binding to the user specified host and port
    server = ThreadedTCPServer((args.host, args.port), ClientHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
