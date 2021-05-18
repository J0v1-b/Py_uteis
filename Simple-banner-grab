#This is a simple banner graber developed in python

#!/usr/bin/python3
import socket

ip = raw_input("Digite o IP: ")
port = input("Digite a porta: ")

meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
meusocket.connect((ip,port))
banner = meusocket.recv(1024)
print banner
