# Assignment1: Introduction to Network Programming

----
私たちのCS
Contact: Sixu Tan, sixu.tan@foxmail.com

----
Welcome to our first assignment! In this assignment, you will work on hands-on problems that guide you to python network programming. Generally, you will have more thorough understanding of the following concepts:
1. Socket
2. What is a server
3. UDP and TCP
4. Handshaking
5. ...

## Task0: Review & Environment Setup
Recap of what we discussed in previous 3 lectures:
* The transport layer mainly consists of TCP and UDP
* TCP is a connection-oriented protocol, which means it requires handshaking.
* UDP is a connectionless protocol, no hanshaking is required, and data transmission is not guaranteed.
* A web server can be seen as a running process.
* TCP Handshaking: SYN, SYNACK and ACK
* A connection address can be identified by IP and port.

### Set up your assisnment
Coming soon...

## Task1: Network programming basic
In this task, you do not need to write any code, but modifying our framework to observe is strongly encouraged. The purpose of this task is to teach you basic network programming framework.

Firstly, start your demo_receiver in a terminal:
```
python demo_receiver.py
```

Then open another terminal, and start the demo sender:
```
python demo_sender.py
```
You will see the following message from the receiver terminal:
```
(base) marsxtan@tansixus-MacBook-Air Sherry_CS % python demo_receiver.py
Waiting for incoming message...
Received from ('127.0.0.1', 4242): Hello, world!
Receiving finished.
```
### Now Your Turn:
1. Read through the 2 demos, try to understand the code logic
2. Are we using TCP or UDP socket in this demo? Why?
3. Can you change the message from the sender to the receiver?
4. If you start the sender before the receiver, what will happen? Why?
## Task2: Client-Server model and toy handshaking
As you have probably noticed, we are using UDP socket, which does not have reliable data transmission or handshaking process. In this task, you are required to implement a toy handshaking process in a simple client-server model.

In a simple client-server model:
> The client requests for a content from the server
> The server provides content

Assumption:
1. The client knows the ip address and port of the server at start
2. The server at start does not know any information of clients. It will record client information when a client connects to it.

### Your turn
1. Read through the framework code *t2_client.py* and *t2_server.py*.
2. Implement the toy handshaking following the comment.
3. Send message from the server to the client!

### Hint
You may be interested in the return value of some functions. The [documents](https://docs.python.org/3/library/socket.html#socket.socket.recvfrom) might be helpful


## Task3: A sub-real web server
Now you have had a basic understanding of UDP socket! In this task, you will learn how TCP socket works in a real-world web server. You do not need to write any code in this task, but you can try modify the code!

Run the server:
```python
python t3_web.py
```
And in your browser, type:
> 127.0.0.1:4242

See if you can see our web page!

### Now your turn
1. Conclude the 3 differences in using UDP and TCP socket.
2. True or False: There can only be 1 socket corresponding to a certain address (ip&port)
3. Can you try edit the content of the web page? What language is used to describe a web page?