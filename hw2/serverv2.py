import socket
import time


BUFFERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 50000))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    from_client = ''

    login_msg = clientsocket.recv(2048)
    from_client += login_msg.decode("utf-8")

    if from_client == 'password':
        msg = "Access Granted"
        clientsocket.send(bytes(msg,"utf-8"))
        
        msg = f"{len(msg):<{BUFFERSIZE}}"+msg
        clientsocket.send(bytes(msg,"utf-8"))
    else:
        break
    
    while True:
        time.sleep(5)
        msg = f"The time is {time.asctime()}"
        msg = f"{len(msg):<{BUFFERSIZE}}"+msg

        print(msg)

        clientsocket.send(bytes(msg,"utf-8"))

fail_msg = "Access Denied"
clientsocket.send(bytes(fail_msg,"utf-8"))
clientsocket.close()
print(f"Connection from {address} has been closed.")
