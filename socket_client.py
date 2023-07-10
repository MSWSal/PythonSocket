import socket


def client_program():
    host = socket.gethostname()  # on same pc
    port = 5034  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to server

    message = input(" Type anything --> ")  # take input

    while message.lower().strip() != 'kill':
        client_socket.send(message.encode())  

        data = client_socket.recv(1024).decode() # receive response

        print('server says: ' + str(data))  

        message = input(" Client reply --> ")  

    client_socket.close()  


if __name__ == '__main__':
    client_program()