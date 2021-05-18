#!/usr/bin/python3
import requests

site = requests.get("url")
status = site.status_code

if (status == 200):
	print("Página ok")
else:
	print("Página inacessível")
