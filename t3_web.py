#####
# A simple web server using TCP instead of UDP. Try to find out differences!
#####

import socket

def handler(client_socket):
    recv_data = client_socket.recv(4096)

    http_header = "HTTP/1.1 200 OK\r\n"+"\r\n"
    http_body = "<h1>Hi Sherry, welcome to our first website!<h1>\r\n"+"<h2>Le vent se lève, il faut tenter de vivre<h2>\r\n"
    http_response = http_header+http_body

    client_socket.send(http_response.encode())
    client_socket.close()

# The ip address and port number of this server. The connection address is defined
# as a tuple of ip and port.
my_ip = "127.0.0.1"
my_port = 4242
my_addr = (my_ip, my_port)

# As a server, we do not know the address of clients in advance.

# Create and bind the server socket to the conenction address above.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(my_addr)
server_socket.listen(11)
print(f"Web server listening on {my_addr}")

while True:
    try:
        client_socket, client_addr = server_socket.accept()
        print(f"Receiving connection from {client_addr}")
        handler(client_socket)
    except Exception:
        server_socket.close()