# Echo server program
import socket
from message import *
print "Server is running"
HOST = 'localhost'                 # Symbolic name meaning all available interfaces
PORT = 9993              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
lol = ''
#lol = raw_input('something')
print "Wait for input..."
conn.recv(1024)
message = Message()
message.response = 'login'
message.username = 'willy'
message.message = 'You are now logged in!'
print "Sending confirmation on logged in..."
conn.send(message.serialize())
##conn.send('lol')
print conn.recv(1024)

while lol != 'exit':
    #lol = raw_input('something')
    print "Wait for input..."
    msg = conn.recv(1024)
    msg = Message()
    message = Message()
    message.response = 'message'
    message.message = 'what ever you typed in'
    print "Sending msg..."
    conn.send(message.serialize())
conn.close()

print "Server is terminated"
