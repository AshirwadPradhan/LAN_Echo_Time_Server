import socket
import time

#create socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host and port
host = socket.gethostname()
port = 9999

#bind...connect()
serversocket.bind((host, port))
#listen()...
serversocket.listen(5)

while True:
    clientsocket, client_addr = serversocket.accept()

    print('Got a connection from {client}'.format(client = client_addr))
    currentTime = time.ctime(time.time()) + '\r\n'
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()

