#!/usr/bin/env python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = '0.0.0.0'
server_port = 1700
hostname = socket.gethostname()

server = (server_address, server_port)
sock.bind(server)
print("Listening on " + server_address + ":" + str(server_port))

while True:
    data, client_address = sock.recvfrom(4096)
    if data:
        response = "Host:%s,  Client address: %s:%s\nData sent by client:\n%s\n" % (
                hostname, client_address[0], client_address[1], data)
        print(response)
        sent = sock.sendto(response.encode(), client_address)
