# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 19:36:12 2020

@author: User
"""

import socket
severPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('',severPort)) 
print("The server is ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    s = message.decode()
    modifiedMesaage = ''.join(str(ord(c)) for c in s)
    serverSocket.sendto(modifiedMesaage.encode(), clientAddress)
