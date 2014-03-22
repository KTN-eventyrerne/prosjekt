'''
KTN-project 2014
'''
#The client application side
#IMPORTANT 1: The message logg from before client logon(this session) 
#shoud be sendt sendt to the cclient after succsessfull login
#the message logg is recived upon login, se place in code marked IMPORTANT 1

#IMPORTANT 2: To use this app, run test.py
#or: 
#instance = Appclient()
#instance.runApp()

#IMPORTANT 3: App run until termination; enter "\logout"

#import
import socket
import time
from client import *
from message import *
import threading


class Appclient(object):

    def __init__(self):
        self.username = ''
        self.port = 1558 #int(raw_input("Port: "))
        self.ip = 'localhost' #raw_input('what ip? '))
        self.client = Client(self.ip, self.port)
	self.run = True
	#self.getinput = True

    def startup(self):
        print 'Hello and welcome to this chatting application!'

#This function is used to run the Appclient instance
    def runApp(self):
	self.startup()
	self.req_username()
	self.thread1 = threading.Thread(target = self.receive_msg)
        self.thread1.setDaemon(True)
        self.thread1.start()
	self.thread2 = threading.Thread(target = self.get_user_input)
        self.thread2.setDaemon(True)
        self.thread2.start()
	while(self.run):
		i = 2

#This function requests a username as input from the user.
#The username is sendt to server.
#Wait until server respond.
#If username is valid, store username and move on.
    def req_username(self):
        #Aslong as we dont have a valid username(not logged in)
        requestUsername = True
        while(requestUsername):
            #Request a username and login to server (send the username to server)
            input = raw_input('Select a user name: ')
            #print "input exepted"
            message = Message()
            message.request = 'login'
            message.username = input
            #print "Sending username"
            self.client.send(message.serialize())
            #print "a message was sendt..."

            #Waiting for a response from server, when response is received, waiting is set to false
            waiting = True
            while (waiting):
                if (self.client.buffer_len())>0: #if any msg in buffer
                    received = self.client.message_pop() #Get message in buffer
		    #print "Received msg: ", received
                    message = Message()
                    message.parse(received)
                    #print "message parsed..."
                    #The different response from server
                    if message.response == 'login':
                        if message.error == 'Invalid username!':
                            print 'Server: ', message.error
                            #print 'Tray a new username!'
                        elif message.error == 'Name allready taken!':
                            print 'Server: ', message.error
                            #print 'Tray a new username!'
                        elif message.error == '':
			    #IMPORTANT 1
			    print 'Server(logg): \n', message.message
                            self.username = message.username
			    print self.username, ': You are now logged in!'
                            requestUsername = False
                    waiting = False


#This function waits for user input and send the message/CMD to the server.
    def get_user_input(self):
	#self.getinput = True
        while(self.run):
	    time.sleep(1)
            input = raw_input()#('Type a message (press enter to send): ')
            if input == '\logout':
                message = Message()
                message.request = 'logout'
		#message.username = self.username
                self.client.send(message.serialize())
		#self.getinput = False
            else:
                message = Message()
                message.request = 'message'
                message.message = input
                self.client.send(message.serialize())


#This function checks the msg buffer in the self.client and if there is a message,
#it acts accordingly...
    def receive_msg(self):
        while(self.run):
            if self.client.buffer_len():
                received = self.client.message_pop()
                message = Message()
                message.parse(received)
                if message.response == 'logout' and message.error == 'Not logged in!':
                    print 'Server: '+ message.error
                    self.run = False
                    #logout_unconfirmed = False
                    #print "logout error"
                elif message.response == 'logout':
                    print self.username, ": You are now logged out..."
                    self.run = False
                    #logout_unconfirmed = False
                    #print "logout sucsess\n"
                elif message.response == 'message' and message.error == 'You are not logged in!':
                    print self.username, ": ", message.error
                    #print "msgError\n"
		elif message.request == 'message' and message.error == '':
		    #print "Test msg\n"
		    print message.message
                else: 
		    print "Msg received, but something whent wrong...."
		    print "The received message: ", message.message




