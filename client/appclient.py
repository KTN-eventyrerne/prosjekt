'''
KTN-project 2013 / 2014
'''
#The client application side

#import
import socket
from client import *
from message import *


class Appclient(object):

    def __init__(self):
        self.username = ''
        self.port = 9999#int(raw_input('what port? '))
        self.ip = 'localhost'#raw_input('what ip? '))
        self.client = Client(self.ip, self.port)

    def startup(self):
        print 'Hello and welcome to this chatting application!'

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
            message = Message()
            message.request = 'login'
            message.username = input
            self.client.send(message.serialize())
            print "debug"

            #Waiting for a response from server, when response is received, waiting is set to false
            waiting = True
            while waiting:
                if self.client.buffer_length():
                    received = self.client.pop_message() #if any msg in buffer
                    message = Message()
                    #message_recieved = self.client.message_received() #Stall until msg recived
                    message.pharse(recieved)
                    #Response
                    if message.response == 'login':
                        if message.error == 'Invalid username!':
                            print message.error
                            print 'Tray a new username!'
                        elif message.error == 'Name allready taken!':
                            print message.error
                            print 'Tray a new username!'
                        elif message.message == 'You are now loged in!':
                            print 'Server: ', message.message
                            self.username = message.username
                            requestUsername = False
                    waiting = False


#This function waits for user input and send the message/CMD to the server.
    def get_user_input(self):
        run = True
        while(run):
            input = raw_input('Type a message (press enter to send): ')
            if input == '\logout':
                message = Message()
                message.request = 'logout'
                self.client.send(message.serialize())
##                logout_unconfirmed
##                while (logout_unconfirmed):
##                    message_recieved = self.client.messegeRecived()
##                    message = Message()
##                    message.pharse(message_recieved)
##                    if message.response == 'logout' and message.error == 'Not logged in!':
##                        print message.error
##                        run = False
##                        logout_unconfirmed = False
##                    else if message.response == 'logout' and message.error == 'Not logged in!':
##                        print 'You are now loged out...'
##                        run = False
##                        logout_unconfirmed = False

            else:
                message = Message()
                message.request = 'message'
                message.message = input
                self.client.send(message.serialize())

#This function checks the msg buffer in the self.client and if there is a message,
#it acts accordingly...
    def recive_msg(self):
        if self.client.buffer_length():
            received = self.client.pop_message()
            message = Message()
            message.pharse(received)
            if message.response == 'logout' and message.error == 'Not logged in!':
                print message.error
                run = False
                logout_unconfirmed = False
            elif message.response == 'logout' and message.error == 'Not logged in!':
                print 'You are now loged out...'
                run = False
                logout_unconfirmed = False
            elif message.response == 'message' and not message.error:
                print message.message
            elif message.response == 'message' and message.error:
                print message.error





