'''
KTN-project 2013 / 2014
'''
#The client application side

#import
import socket
from client import *
from message import *


class Appclient(object):
    
    #Start up
    print "Hello and welcome!"
    client = Client()

    def req_username(client):
        requestUsername = False
        while(requestUsername):
            input = raw_input('Select a user name: ')
            message = Message()
            message.request = "login"
            message.username = input
            client.send(message.serialize())
            message = Message()
            client.message_received

    





