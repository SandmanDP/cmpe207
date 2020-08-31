from socket import AF_UNSPEC, SOCK_STREAM, getaddrinfo, socket
import time


af, socktype, proto, _, sa = getaddrinfo('2a02:898:17:8000::42', 23, AF_UNSPEC, SOCK_STREAM)[0]
with socket(af, socktype, proto) as s:
    s.connect(sa)
    time.sleep(5)
    data = s.recv(1024)

print(data.decode("utf-8"))
