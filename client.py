import socket

def tcp_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server's address and port
    server_address = ('localhost', 12345)
    client_socket.connect(server_address)
    print('Connected to {}:{}'.format(*server_address))

    try:
        # Send data to the server
        message = '1111101011101110010111110101111110101001'
        client_socket.sendall(message.encode())
        print('Sent message: {}'.format(message))

        # Receive the server's response
        response = client_socket.recv(1024)
        print('Received response: {}'.format(response.decode()))

    except Exception as e:
        print('Error occurred: {}'.format(e))

    finally:
        # Close the socket
        client_socket.close()
        print('Connection closed')

if __name__ == '__main__':
    tcp_client()
