#Simple Python script to send USER and PASSWORD
#Usage: ./Simple-data-sender.py <IP> <PORT>

#!/usr/bin/python3
import socket

ip = raw_input("Digite o IP: ")
port = input("Digite a porta: ")

meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "enviando usuário:"
meusocket.send("USER <USER>\r\n") #Change <USER>
banner = meusocket.recv(1024)
print banner

print "enviando senha:"
meusocket.send("PASS <PASSWORD>\r\n") #Change <PASSWORD>
banner = meusocket.recv(1024)
print banner
