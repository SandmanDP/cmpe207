import socket
import time


BUFFERSIZE = 10
port = 50000
password = "password"
s = None
client = None


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", port))
    print(f'Server launched on port {port}! Password is `{password}`')


    while True:
        s.listen(1)
        # now our endpoint knows about the OTHER endpoint.
        print("Listening for a new connection...")
        client, address = s.accept()
        print(f"Connection from {address} has been established!")
        time.sleep(0.5)
        client.send(bytes("Password: \x1b[30;40m", "utf-8"))
        try:
            login_msg = client.recv(2048)
            client.send(bytes("\x1b[0m","utf-8"))
            from_client = login_msg.decode("utf-8")

            if from_client.rstrip('\n\r') == 'password':
                msg = "Access Granted! Starting time service\n"
                client.send(bytes(msg,"utf-8"))

                last_time = ''
                while True:
                    new_time = time.asctime()
                    if new_time != last_time:
                        last_time = new_time
                        client.send(bytes(f"\x1b[2K\rThe time is {new_time}", "utf-8"))
                    time.sleep(0.05)
            else:
                client.send(bytes("Access Denied!", "utf-8"))
                client.close()
        except BrokenPipeError:
            break
        finally:
            print(f"Connection from {address} has been closed.")
except KeyboardInterrupt:
    if client:
        client.close()
    if s:
        s.close()
