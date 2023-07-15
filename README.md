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
2. Can you change the message from the sender to the receiver?
3. If you start the sender before the receiver, what will happen? Why?
## Task2: Client-Server model and top handshaking
Read the t2 code and comment.
## Task3: A sub-real web server