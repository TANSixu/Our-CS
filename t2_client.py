#####
# The framework for your client.
#####

import socket

# The ip address and port number of this client. The connection address is defined
# as a tuple of ip and port.
my_ip = "127.0.0.1"
my_port = 4242
my_addr = (my_ip, my_port)

# Assume that our client knows the address of the server.
dest_ip = "127.0.0.1"
dest_port = 4243
dest_addr = (dest_ip, dest_port)

# Create and bind the client socket to the conenction address above.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.bind(my_addr)

#############################################
# Your turn!!!!!!!!
# Use the utilities above, finish your client!
#############################################

# Step 0. Send SYN to the server to start a connection

# Step 1. If receive SYNACK from the server, send ACK to the server

# Step 2. Reveive message from the server and print out.

# Always remember to close socket after using to release resources.
client_socket.close()