# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 19:19:07 2020

@author: User
"""

import socket
serverName = "127.0.0.1"
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input("Input lowercase or uppercase sentence, and it will be convert to ASCii:")
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
