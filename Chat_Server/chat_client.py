import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
print(type(host))
port = 9999

sock.connect((host, port))
tm = sock.recv(1024)

sock.close()
print('The server time is {}'.format(tm.decode('ascii')))
