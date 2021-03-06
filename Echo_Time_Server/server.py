import socket
import time
import threading


class Server():
    '''
    Server Class to create a server and listen to client
    '''
    def __init__(self):
        '''
        initializing the socket, host and port
        '''
        self.server_sock = socket.socket(socket.AF_INET,
                            socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.time_port = 9999
        self.echo_port = 11223

    def set_time_connection(self):
        '''
        method to set up a connection
        '''
        try:
            self.server_sock.bind((self.host, self.time_port))
            self.server_sock.listen(10)
        except ConnectionError:
            print('Cannot create a connection')

    def set_echo_connection(self):
        '''
        method to set up a connection
        '''
        try:
            self.server_sock.bind((self.host, self.echo_port))
            self.server_sock.listen(10)
        except ConnectionError:
            print('Cannot create a connection')

    def time_services(self):
        '''
        method to serve current time
        '''
        try:
            while True:
                client_sock, client_addr = self.server_sock.accept()
                print('Client {client} connected to time service:'.
                    format(client=client_addr))

                currentTime = time.ctime(time.time()) + '\r\n'

                try:
                    client_sock.send(currentTime.encode('ascii'))
                    client_sock.close()
                except ConnectionError:
                    print('Client not reachable')
        except KeyboardInterrupt:
            print('Interrupted')

    def echo_services(self):
        '''
        method to serve echo service
        '''
        try:
            while True:
                client_sock, client_addr = self.server_sock.accept()
                print('Client {client} connected to echo service:'.
                    format(client=client_addr))

                msg = client_sock.recv(1024)
                if not msg:
                    break
                try:
                    #client_sock.sendall(msg.encode('ascii'))
                    client_sock.sendall(msg)
                except ConnectionError:
                    print('Client not reachable')
                finally:
                    client_sock.close()
        except KeyboardInterrupt:
            print('Interrupted')



if __name__ == '__main__':
    time_server = Server()
    echo_server = Server()
    th1 = threading.Thread(target=echo_server.echo_services)
    th2 = threading.Thread(target=time_server.time_services)
    echo_server.set_echo_connection()
    time_server.set_time_connection()
    th1.start()
    th2.start()

    th1.join()
    th2.join()
    # echo_server.echo_services()
    # time_server.time_services()
    print('Completed')
