#####
# This is a demo of sender instructing on how to use UDP socket in python to
# send a helloworld message to a certain address.
# Have fun!
#####

import socket

# The ip address and port number of this sender. The connection address is defined
# as a tuple of ip and port.
my_ip = "127.0.0.1"
my_port = 4242
my_addr = (my_ip, my_port)

# Create and bind the sender socket to the conenction address above.
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sender_socket.bind(my_addr)

# Destination ip, port, and connection address. This is where we are gonna send our
# message to.
dest_ip = "127.0.0.1"
dest_port = 4243
dest_addr = (dest_ip, dest_port)

# Sending
sender_socket.sendto("Hello, world!".encode(), dest_addr)
print("sender sending finished.")

# Always remember to close socket after using to release resources.
sender_socket.close()
