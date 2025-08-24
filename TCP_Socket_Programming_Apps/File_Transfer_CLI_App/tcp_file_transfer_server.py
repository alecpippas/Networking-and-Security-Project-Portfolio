# Server-side Implementation of File Transfer Application

# Client is KALI Host from Area 0
# Server is R3 from Area 1 

import socketserver
import time as t

# Socket Configuration ------------------------------------------------------------
IP_ADDRESS = "10.10.11.2"
PORT = 5500
# ---------------------------------------------------------------------------------


class FileHandler(socketserver.BaseRequestHandler):
        def handle(self):  #override the handle method

            client_IP, client_port = self.client_address
            current_time = t.strftime("%H:%M:%S", t.localtime())

            filename = "client_" + str(client_IP) + "_file_" + current_time  
            with open(filename, 'wb') as f:
                while True:
                    frag = self.request.recv(10240)
                    if not frag: #if recv() returns an empty string (implying the connection is terminated)
                        break
                    #write fragment to the file
                    f.write(frag)
                print("File transfer complete.")
                print('File save as:', filename)

                
                        
                
if __name__ == "__main__":
    server = socketserver.TCPServer((IP_ADDRESS, PORT), FileHandler)
    try:
        server.serve_forever()
    except Exception as e:
        print(e)
    finally:
        server.shutdown()
        server.server_close()