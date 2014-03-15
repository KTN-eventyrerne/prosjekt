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
        while 1:
            try:
                if recv:
                    raw = get_msg()
                    msg = parsed(raw)
                    handle_request(msg)
            else:
            print 'Client disconnected!'

    def handle_request(self, msg):
        if msg.request is login:
            if is_illegal(username):
                respond_illegal(msg)
            else if is_taken(username):
                respond_taken(msg)
            else
                add_client(msg.username)
                respond_success(msg)
            else if msg.request is 'message':
                send_to_all(msg)
            else if msg.request is 'logout':
                remove_client()

    def is_illegal(self, string username):
        legal_chars = set('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ_')
        for c in username:
            if c not in legal_chars:
                return true
        return false
    
    def respond_illegal(self, msg):
            
    def is_taken(self, string username):
            
    def respond_taken(self, msg):
