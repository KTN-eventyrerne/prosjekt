import SocketServer

import sys
sys.path.append('../')
import Message

'''
The RequestHandler class for our server.

It is instantiated once per connection to the server, and must
override the handle() method to implement communication to the
client.
'''

class ClientHandler(SocketServer.BaseRequestHandler):
    def __init__(self):
        users = []

    def valid_username(self, name):
        import re
        return re.match('^\w+$', name)


    def available_username(self, name):
        return name not in users

    def handle(self):
        # Get a reference to the socket object
        self.connection = self.request
        # Get the remote ip adress of the socket
        self.ip = self.client_address[0]
        # Get the remote port number of the socket
        self.port = self.client_address[1]
        print 'Client connected @' + self.ip + ':' + str(self.port)
		while 1:
			# Wait for data from the client
			data = self.connection.recv(1024).strip()
			# Check if the data exists
			# (recv could have returned due to a disconnect)
			if data:
				msg = Message()
				msg.parse(data)
				handle_request(msg)
			else:
				print 'Client disconnected!'

    def handle_request(msg):
        if msg.request is login:
            if not valid_username(username):
                respond_illegal(msg)
            else if not available_username(username):
                respond_taken(msg)
            else{
                add_client(msg.username)
                respond_success(msg)
        }
        else if msg.request is 'message'{
            send_to_all(msg)
        }
        else if msg.request is 'logout'{
            remove_client()
        }
    }

    def respond_illegal(self, msg):
		resp = Message()
		resp.response = 'login'
		resp.error = 'Invalid username!'
		resp.username = msg.username
		resp.seialize() 
		#TODO: send
    def respond_taken(self, msg):
			
