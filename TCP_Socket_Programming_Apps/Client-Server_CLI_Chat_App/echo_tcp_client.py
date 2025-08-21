# Client-side Implementation of Client-Server CLI Chat App

# Client is KALI Host from Area 0
# Server is R3 from Area 1 

# Client machine was running Python 2.7, hence the code is written in Python 2.7 syntax

from socket import socket, AF_INET, SOCK_STREAM
import sys

def client_secret_message_TCP():
    """Establish a TCP connection with a remote server and send a secret message to the server and display the $"""
    server_IP, server_port = ('10.10.11.2', 4500)

    #create a client socket that uses the AF_INET (IPv4 address family) and is of the SOCK_STREAM (TCP) socket $
    client_sock = socket(AF_INET, SOCK_STREAM)

    #connect to the remote server and have Client OS automatically assign network interface and ephemeral port $
    client_sock.connect((server_IP, server_port))

    while True:
        #get message from the user on the command line
        message = raw_input("Enter Message: ").strip()

        if message.lower() in ('q', 'quit', 'quit()', 'close', 'close()'):
            break
        else:
            #send message to remote server; sendall() ensures the entire byte stream argument is sent to the se$
            #message is encoded from UTF-8 Unicode to Byte String
            message += '\n'
            client_sock.sendall(message.encode('utf-8'))
            print "Sent:", message

            #recv() is called repeatedly until all message fragments are received
            #message frag is decoded from byte stream to UTF-8 Unicode
            response_buffer = ""
            while True:
                frag = client_sock.recv(10240)
                if not frag: #if recv() returns an empty string (implying server ended connection)
                    break
                response_buffer += frag.decode('utf-8')
                if '\n' in response_buffer:
                    response, response_buffer = response_buffer.split('\n', 1)
                    print "Received:", response
                    print
                    print '\n'
                    break

    #actively close socket, terminating the TCP connection and releasing system resources after user quits the $
    client_sock.close()

if __name__  ==  "__main__":
    client_secret_message_TCP()