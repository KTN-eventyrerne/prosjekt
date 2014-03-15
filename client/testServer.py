# Echo server program
import socket

HOST = 'localhost'                 # Symbolic name meaning all available interfaces
PORT = 9999              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
lol = ''
while lol != 'exit':
    lol = raw_input('something')
    conn.send(lol)
conn.close()
