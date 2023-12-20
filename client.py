#!/usr/bin/env python3

import socket
import threading
from blockchain import Blockchain
#import pickle SEND objects


class Client:

	def __init__(self,serverip):
		SERVER = serverip
		self.DISCONNECT = "DISCONNECT"
		self.HEADER = 64
		#print(socket.gethostbyname())
		#print(socket.gethostbyname(socket.gethostname()))
		PORT = 5050
		self.ADDR = (SERVER, PORT)
		self.FORMAT = 'utf-8'


		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	


	def send(self,msg):
		self.client.connect(self.ADDR)
		message = msg.encode(self.FORMAT)
		msg_len = len(message)
		send_len = str(msg_len).encode(self.FORMAT)
		send_len += b' ' * (self.HEADER - len(send_len))
		self.client.send(send_len)
		self.client.send(message)
		
		
c = Client("127.0.1.1")
c.send("HELLO WORLD!")
blockchain = Blockchain()
def replace_the_chain():
    is_chain_replaced = blockchain.replace_chain()
    if is_chain_replaced:
        response = {'message': 'Chain is replace', 'New chain':blockchain.chain} 
    else:
        response =  {'message':'chain is the longest','Longest chain': blockchain.chain}
    
    return response
print(replace_the_chain())

