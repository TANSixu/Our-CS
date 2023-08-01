#####
# This is a demo of receiver instructing on how to use UDP socket in python to
# receive a helloworld message from another socket.
# Have fun!
#####

import socket

# The ip address and port number of this receiver. The connection address is defined
# as a tuple of ip and port.
my_ip = "127.0.0.1"
my_port = 4243
my_addr = (my_ip, my_port)

# Create and bind the receiver socket to the conenction address above.
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver_socket.bind(my_addr)

# Receiving
print("Waiting for incoming message...")
data, from_addr = receiver_socket.recvfrom(1024)
print(f"Received from {from_addr}: {data.decode()}")
print("Receiving finished.")
# Always remember to close socket after using to release resources.
receiver_socket.close()