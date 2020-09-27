import socket

BUFFERSIZE = 10

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 50000))

access_msg = input("Please enter password to obtain access: ")
client.send(bytes(access_msg,"utf-8"))

server_msg = ''
server_msg = client.recv(16)
full_server_msg = server_msg.decode("utf-8")
#print(full_server_msg)

if full_server_msg == 'Access Granted':

    while True:
        full_msg = ''
        new_msg = True
        while True:
            msg = client.recv(16)
            if new_msg:
                print("new msg len:",msg[:BUFFERSIZE])
                msglen = int(msg[:BUFFERSIZE])
                print(f"full message length: {msglen}")
                new_msg = False

            full_msg += msg.decode("utf-8")

            # print(len(full_msg))

            if len(full_msg)-BUFFERSIZE == msglen:
                print("full message received")
                print(full_msg[BUFFERSIZE:])
                new_msg = True
                full_msg = ""
else:
    print(full_server_msg)
    client.close()
