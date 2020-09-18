import socket
import time

HOST = '94.142.241.111' # The server's hostname or IP address
PORT = 23               # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

full_msg = ''
# multiply 60 by real number to receive more or less data
end_time = time.time() + 60
while True:
    msg = s.recv(1024)
    if time.time() > end_time:
        break
    if len(msg) <= 0:
        break
    full_msg += msg.decode('ascii')
print(full_msg)
