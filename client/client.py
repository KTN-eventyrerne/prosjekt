import socket
import threading


class Client():
    def __init__(self, host, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((host, port))
        self.connection.settimeout(2)

        self.exit = False
        self.ko = []
        self.lock = threading.Lock()
        
        self.thread = threading.Thread(target = self.recieve)
        self.thread.setDaemon(True)
        self.thread.start()


    def recieve(self):
        while(self.exit == False):
            try:
                self.lock.acquire()
                received_data = self.connection.recv(1024)
                self.ko.append(received_data)
            except:
                pass
            finally:
                self.lock.release()

    def buffer_len(self):
        self.lock.acquire()
        length = len(self.ko)
        self.lock.release()
        return length

    def message_pop(self):#, message, connection):
        self.lock.acquire()
        ret = ''
        if(len(self.ko) != 0):
            ret = self.ko.pop(0)
        self.lock.release()
        return ret

    def connection_closed(self):
        self.exit = True
        self.thread.join()
        self.connection.close()

    def send(self, data):
        #self.lock.acquire()
        self.connection.sendall(data)
        #self.lock.release()
