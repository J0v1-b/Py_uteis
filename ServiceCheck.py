#!/usr/bin/python3
import urllib

site = urllib.urlopen("url")
server = site.info()

print "O servidor web está rodando"
print server['Server']
