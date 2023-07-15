#####
# The framework for your server.
#####

import socket

# The ip address and port number of this server. The connection address is defined
# as a tuple of ip and port.
my_ip = "127.0.0.1"
my_port = 4243
my_addr = (my_ip, my_port)

# As a server, we do not know the address of clients in advance.

# Create and bind the server socket to the conenction address above.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(my_addr)

#############################################
# Your turn!!!!!!!!
# Use the utilities above, finish your server!
#############################################

# Step 0. Waiting for SYN.

# Step 1. If receive SYN, record the address of the client, and reply SYNACK

# Step 2. Upon receiving ACK, connection established. Send the message to the client.

message = "Let's meet in the dream No.4242!"

# Always remember to close socket after using to release resources.
server_socket.close()