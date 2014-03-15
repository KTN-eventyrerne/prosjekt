#import
import socket
from threading import Thread
import thread
from client import *
from appclient import *
#sys.path.append('\..\')
from message import *


print "Test program is running."
test = Appclient()
print "===================Test login=============="
test.req_username()
print "===================Test login==============END===="
thread.start_new_thread(test.receive_msg, ())

test.get_user_input()

print "Test program has been terminated..."
