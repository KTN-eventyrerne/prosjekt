import SocketServer
import threading
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
				lock.acquire()
				self.server.remove_client(self, self.nickname)
				lock.release()
				print 'Client disconnected!'

    def handle_request(self, msg):
        if msg.request is 'login':
            if not self.valid_username(msg.username):
                self.respond_illegal(msg)
                return
            if not self.available_username(msg.username):
                self.resp_username_taken(msg)
                return
            self.resp_login_success(msg)
            return

        if msg.request is 'message':
			lock.acquire()
            self.server.send_to_all(msg)
			lock.release()

            return

        if msg.request is 'logout':
            self.remove_client()
            return
			
	def send_to_client(self, msg):
		m = Message()
		m.response = 'message'
		m.message = msg
		m.serialize() 
		self.connection.sendall(m)
		
	def resp_login_success(self, msg):
		self.username = msg.username
		#update the servers list of clients
		lock.acquire()
		self.server.add_client(self, self.username)
		history = self.server.get_messages()
		lock.release()
		#send response to client
		resp = Message()
		resp.response = 'login'
		resp.username = msg.username
		resp.messages = history
		resp.serialize() 
		self.connection.sendall(resp)
		
    def resp_username_illegal(self, msg):
		resp = Message()
		resp.response = 'login'
		resp.error = 'Invalid username!'
		resp.username = msg.username
		resp.serialize() 
		self.connection.sendall(resp)

    def resp_username_taken(self, msg):
		resp = Message()
		resp.response = 'login'
		resp.error = 'Name already taken!'
		resp.username = msg.username
		resp.serialize() 
		self.connection.sendall(resp)
			
