import socket


def server_program():
    
    host = socket.gethostname() #get the host name
    port = 5034  #init the port

    server_socket = socket.socket()  # instantiate a socket
    server_socket.bind((host, port))  # bind host and port 

    server_socket.listen(2)  #can listen for 2
    print("Waiting for clients...")

    connection, address = server_socket.accept()  
    print("Call from: " + str(address))
    while True:
        data = connection.recv(1024).decode()  #wont receive more than 1024bytes
        if not data:
            break
        print("Client says: " + str(data))
        data = input(' Type a reply --> ')
        connection.send(data.encode())  # send data to client

    connection.close()  


if __name__ == '__main__':
    server_program()