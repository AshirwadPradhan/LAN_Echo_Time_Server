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
        except OSError:
            print('Client socket disconnected')

    def get_echo_services(self):
        '''
        connect to the echo service port of the server
        '''
        msg = b'Hello World'
        try:
            self.client_sock.sendall(msg)
            serv_msg = self.client_sock.recv(1024)
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
        print('The server time is {time}'.format(
            time=serv_time.decode('ascii')))

    def teardown_connection(self):
        '''
        close the connction
        '''
        self.client_sock.close()


if __name__ == '__main__':

    choice = ''

    while(choice != 'esc'):
        print('\n')
        print('Services Offered')
        print('Enter E for echo service')
        print('Enter T for time service')
        print('Enter "esc" to quit\n')
        choice = input()

        if choice.lower() == 'e':
            echo_client = Client()
            echo_client.set_echo_connection()
            echo_client.get_echo_services()
            echo_client.teardown_connection()
        elif choice.lower() == 't':
            time_client = Client()
            time_client.set_time_connection()
            time_client.get_time_services()
            time_client.teardown_connection()
        elif choice.lower() == 'esc':
            break
        else:
            print('Wrong choice')
        



    