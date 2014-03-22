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
test.runApp()
#test.startup()
#test.req_username()
#thread.start_new_thread(test.receive_msg, ())
#thread.start_new_thread(test.get_user_input, ())
#test.get_user_input()
#while(run):

print "Test program has been terminated..."
