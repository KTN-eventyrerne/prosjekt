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

    def startup(self):
        print 'Hello and welcome to this chatting application!'

#This function requests a username as input from the user.
#The username is sendt to server.
#Wait until server respond.
#If username is valid, store username and move on.
    def req_username(self, client):
        #Aslong as we dont have a valid username(not logged in)
        requestUsername = True
        while(requestUsername):
            #Request a username and login to server (send the username to server)
            input = raw_input('Select a user name: ')
            message = Message()
            message.request = 'login'
            message.username = input
            client.send(message.serialize())

            #Waiting for a response from server, when response is received, waiting is set to false
            waiting = True
            while waiting:
                received = client.pop_message() #if any msg in buffer
                if received:
                    message = Message()
                    #message_recieved = client.message_received() #Stall until msg recived
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
    def get_user_input(self, client):
        run = True
        while(run):
            input = raw_input('Type a message (press enter to send): ')
            if input == '\logout':
                message = Message()
                message.request = 'logout'
                client.send(message.serialize())
##                logout_unconfirmed
##                while (logout_unconfirmed):
##                    message_recieved = client.messegeRecived()
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
                client.send(message.serialize())

#This function checks the msg buffer in the client and if there is a message,
#it acts accordingly...
    def recive_msg(self, client):
        received = client.pop_message()
        if received:
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







