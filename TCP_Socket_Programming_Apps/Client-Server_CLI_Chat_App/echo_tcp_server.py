# Server-side Implementation of Client-Server CLI Chat App

# Client is KALI Host from Area 0
# Server is R3 from Area 1 

# Virtual Servers were running Python 2.7, hence the code is written in Python 2.7

import SocketServer

class SecretMessageHandler(SocketServer.BaseRequestHandler):
    def handle(self): #override the handle method

        request_buffer = ""
        #listen to requests indefinitely untill client terminates TCP connection
        while True:
            frag = self.request.recv(10240)
            if not frag: #if recv() returns an empty string (implying the connection is terminated)
                break
            request_buffer += frag.decode('utf-8')
            #process earliest request
            while '\n' in request_buffer:
                request, request_buffer = request_buffer.split('\n', 1)
                print "Received message:", request

                digits = ""
                digit_count = 0
                if "SECRET" in request:
                    for char in range(len(request)):
                        if request[char].isdigit() == True:
                            digits += request[char]
                            digit_count += 1
                    response = "Digits: " + digits + " Count: " + str(digit_count)
                else:
                    response = "Secret code not found."

                print "Sending Response:", response
                response += '\n'
                self.request.sendall(response.encode('utf-8'))


if __name__ == "__main__":
    server = SocketServer.TCPServer(("10.10.11.2", 4500), SecretMessageHandler)
    try:
        server.serve_forever()
    except Exception as e:
        print e
    finally:
        server.shutdown()
        server.server_close()