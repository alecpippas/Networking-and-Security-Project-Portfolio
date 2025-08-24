# Client-side Implementation of File Transfer Application

# Client is KALI Host from Area 0
# Server is R3 from Area 1 

from socket import socket, AF_INET, SOCK_STREAM
import sys

# Socket Configuration ------------------------------------------------------------
IP_ADDRESS = "10.10.11.2"
PORT = 5500
# ---------------------------------------------------------------------------------

def send_file_TCP ():
    """Establish a TCP connection with a remote server and send a secret message to the server and display the response"""
    server_IP, server_port = (IP_ADDRESS, PORT)

    #create a client socket that uses the AF_INET (IPv4 address family) and is of the SOCK_STREAM (TCP) socket type
    client_sock = socket(AF_INET, SOCK_STREAM)

    #connect to the remote server and have client OS automatically assign network interface and ephemeral port
    client_sock.connect((server_IP, server_port))

    #get the filename from the command line
    filename = sys.argv[1]

    #open file in 'r' read mode and 'b' binary mode
    with open(filename, 'rb') as file:
        
        while True:
            #10MB read buffer
            chunk = file.read(1048576)
            if not chunk:
                break
            client_sock.sendall(chunk)

    #actively close socket, terminating the TCP connection and releasing system resources after user quits the program
    client_sock.close()


if __name__ == "__main__":
    send_file_TCP()
