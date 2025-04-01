import socket

asock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
asock.connect(("google.com", 80))
