#  coding: utf-8 
import socketserver, os

# Copyright 2013 Abram Hindle, Eddie Antonio Santos
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# Furthermore it is derived from the Python documentation examples thus
# some of the code is Copyright © 2001-2013 Python Software
# Foundation; All Rights Reserved
#
# http://docs.python.org/2/library/socketserver.html
#
# run: python freetests.py

# try: curl -v -X GET http://127.0.0.1:8080/


class MyWebServer(socketserver.BaseRequestHandler):
    
    def handle(self):
        self.data = self.request.recv(1024).strip()
        # print ("Got a request of: %s\n" % self.data)

        # Parse the data 
        request = self.data.decode("utf-8").split("\r\n") 
        request = request[0].split() # ['GET', path, 'HTTP/1.1']

        self.method = request[0]
        self.path = request[1]
        self.version = request[2]



        if self.method.upper() != "GET":
            # send 405 Method Not Allowed
            self.send_error("405 Method Not Allowed")
        
        # self.request.sendall(bytearray("OK",'utf-8'))
    
    def send_error(self, status, path_location = ""):
        error = self.version + status + "\r\nDate: " + date + "\r\n" + path_location + "Content-Length: " + content_length + "\r\nContent-Type:" + content_type + "\r\n" + "Connection: close\r\n\r\n"
        self.request.sendall(bytearray(error,'utf-8'))

if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    socketserver.TCPServer.allow_reuse_address = True
    # Create the server, binding to localhost on port 8080
    server = socketserver.TCPServer((HOST, PORT), MyWebServer)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
