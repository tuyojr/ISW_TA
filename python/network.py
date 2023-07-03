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