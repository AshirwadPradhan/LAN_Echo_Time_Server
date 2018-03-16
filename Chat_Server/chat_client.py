import socket


class Client():
    '''
    class to create cient and request for services
    '''
    def __init__(self):
        '''
        initialize socket, host and port
        '''
        self.client_sock = socket.socket(socket.AF_INET,
            socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.time_port = 9999
        self.echo_port = 11223

    def set_time_connection(self):
        '''
        connect to the time service
        '''
        try:
            self.client_sock.connect((self.host, self.time_port))
        except ConnectionRefusedError:
            print('Server is Unreachable')

    def set_echo_connection(self):
        '''
        connect to the echo service
        '''
        try:
            self.client_sock.connect((self.host, self.echo_port))
        except ConnectionRefusedError:
            print('Server is Unreachable')

    def get_echo_services(self):
        '''
        connect to the echo service port of the server
        '''
        msg = b'Hello World'
        try:
            self.client_sock.sendall(msg)
            serv_msg = self.client_sock.recv(1024)
            self.client_sock.close()
        except OSError:
            print('No address supplied')
        else:
            print('Data Echoed : {data}'.format(
                data=serv_msg))

    def get_time_services(self):
        '''
        connect to the time service port of the server
        '''
        serv_time = self.client_sock.recv(1024)
        self.client_sock.close()
        print('The server time is {time}'.format(
            time=serv_time.decode('ascii')))


if __name__ == '__main__':
    client = Client()
    # client.set_time_connection()
    # client.get_time_services()
    client.set_echo_connection()
    client.get_echo_services()
