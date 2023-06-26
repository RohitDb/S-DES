import socket

def tcp_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)
    print('Server is listening on {}:{}'.format(*server_address))

    while True:
        # Wait for a connection
        print('Waiting for a connection...')
        client_socket, client_address = server_socket.accept()
        print('Accepted connection from {}:{}'.format(*client_address))

        try:
            # Receive data from the client
            data = client_socket.recv(1024)
            received_bits = data.decode()
            print('Received bits: {}'.format(received_bits))
            # Send a response back to the client
            response = 'Hello from the server!'
            client_socket.sendall(response.encode())
            print('Sent response: {}'.format(response))

        except Exception as e:
            print('Error occurred: {}'.format(e))

        finally:
            # Close the connection
            client_socket.close()
            print('Connection with {}:{} closed'.format(*client_address))

if __name__ == '__main__':
    tcp_server()
