# Echo server program
import socket
from message import *
print "testServer is running..."
HOST = 'localhost'
PORT = 1558 #int(raw_input("Port: "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
print "Wait for input..."
conn.recv(1024)
message = Message()
message.response = 'login'
message.username = 'willy'
message.message = '\nHei\nHva er det du sier?\nHar det rabla for deg?\nNemen er det deg!\n'
print "Sending confirmation on logged in..."
conn.send(message.serialize())
#print conn.recv(1024)
print "Login completed..."
test = True
i = 0
while test:
   	print("Wait for input...")
    	msg = conn.recv(1024)
	while i < 100:
		i = i + 1
	print "msg: " + msg
    	conn.send(msg)

	#Read
	message = Message()
	message.parse(msg)

	#If message empty, terminate testServer
	if message.message == 0:
		test = False

	#If logout requested, grant logout...
	if message.request == 'logout':
		message = Message()
		message.response = 'logout'
		message.username = 'willy'
		print "Sending confirmation on logout..."
		conn.send(message.serialize())
conn.close()
print "testServer is terminated..."
