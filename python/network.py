# # tcp_server.py
# # server side
# import socket # imports the socket module

# s = socket.socket() # creates a socket object
# host = "192.168.45.120" # gets the local machine name (server name)
# port = 5000 # reserve a port for your service to connect on

# s.bind((host, port)) # binds to the port
# print("Waiting for connection...") 
# s.listen(5) # listens for connections

# while True:
#     conn, addr = s.accept() # establishes connection with client
#     print("Got Connection From", addr)
#     conn.send("Server Saying Hi".encode())
#     conn.close() # closes the connection

# # client side
# import socket

# s = socket.socket()
# host = "192.168.45.120"
# port = 1025

# s.connect((host, port))
# print(s.recv(1024).decode())
# s.close()

# # server side
# import socket # imports the socket module

# def server_program():
#     host = "192.168.45.120" # gets the local machine name (server name)
#     port = 1025 # reserve a port for your service to connect on

#     s = socket.socket() # creates a socket object
#     s.bind((host, port)) # binds to the port

#     s.listen(2) # listens for connections
#     conn, addr = s.accept() # establishes connection with client
#     print("Connection from:" + str(addr))

#     while True:
#         # receive data stream. it wont accept
#         data = conn.recv(1024).decode()
#         if not data:
#             # if data is not received, break
#             break
#         print("from connected user: " + str(data))
#         data = input(" -> ")
#         conn.send(data.encode()) # send data to the client
#     conn.close() # closes the connection
# if __name__ == '__main__':
#     server_program()

# # client side
# import socket # imports the socket module

# def client_program():
#     host = "192.168.45.120" # gets the local machine name (server name)
#     port = 1025 # reserve a port for your service to connect on

#     s = socket.socket() # creates a socket object
#     s.connect((host, port)) # connects to the server

#     message = input(" -> ") # takes input

#     while message.lower().strip() != 'bye':
#         s.send(message.encode())
#         data = s.recv(1024).decode()

#         print("Received from server: " + data)

#         message = input(" -> ")
    
#     s.close() # closes the connection

# if __name__ == '__main__':
#     client_program()