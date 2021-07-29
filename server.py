import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

bind_address = "0.0.0.0"
bind_port = 9560

server = (bind_address, bind_port)
print("Starting server on " + bind_address + ":" + str(bind_port))

sock.bind(server)

sock.listen(1)

while True:
    print("waiting...")
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()