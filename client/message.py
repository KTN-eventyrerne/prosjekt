import json
from StringIO import StringIO

class Message(object):

    def __init__(self):
        self.request = ''
        self.message = ''
        self.response = ''
        self.error = ''
        self.username = ''

    def parse(self, msg):
        message = json.loads(msg)
        self.request = message[0].get('request', '')
        self.message = message[0].get('message', '')
        self.response = message[0].get('response', '')
        self.error = message[0].get('error', '')
        self.username = message[0].get('username', '')
        self.validate()

    def serialize(self):
        self.validate()
        jmsg = {}
        if(self.request != ''):
            jmsg.update({'request': self.request})
        if(self.message != ''):
            jmsg.update({'message': self.message})
        if(self.response != ''):
            jmsg.update({'response': self.response})
        if(self.error != ''):
            jmsg.update({'error': self.error})
        if(self.username != ''):
            jmsg.update({'username': self.username})
        return json.dumps([jmsg])

    def validate(self):
        if(self.request == '' and self.response == ''):
            raise Exception('No request or response field defined')
        if(self.request != '' and self.response != ''):
            raise Exception('Both request and response field defined')
        if(self.message == '' and self.username == '' and self.error == '' and self.request != 'logout'):
            raise Exception('No message, username nor error. No payload in message')
