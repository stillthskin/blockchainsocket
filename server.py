#!/usr/bin/env python3

import socket
import threading
from uuid import uuid4
from blockchain import Blockchain
#import pickle SEND objects


class Server:
	def __init__(self):
		self.DISCONNECT = "DISCONNECT"
		self.HEADER = 64
		SERVER = socket.gethostbyname(socket.gethostname())
		print(socket.gethostbyname(socket.gethostname()))
		PORT = 5050
		self.ADDR = (SERVER, PORT)
		self.FORMAT = 'utf-8'
		self.addr = " "
		self.b = Blockchain()
		self.b.add_node(SERVER)

		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)





	def handle_client(self, conn, addr):
		print(f'{addr[0]} Connected')
		addr = addr[0]
		connected = True
		self.b.add_node(addr)
		
		while connected:
			msg_len = conn.recv(self.HEADER).decode(self.FORMAT)
			if msg_len:
				msg_len = int(msg_len)
				msg = conn.recv(msg_len).decode(self.FORMAT)
				if msg == self.DISCONNECT:
					break
				print(f'Message {msg} Address {addr}')
				print(f'The nodes: {self.b.nodes}')
		#conn.close()

	def start(self):
		self.server.bind(self.ADDR)
		self.server.listen()
		while True:
			conn, addr = self.server.accept()
			thread = threading.Thread(target=self.handle_client, args=(conn, addr))
			thread.start()
			print(f'Active Threads: {threading.active_count() - 1}')
			return
	
s = Server()
node_address = str(uuid4()).replace('-', '')
blockchain = Blockchain()
def mine_block():
    prev_block = blockchain.get_last_block()
    prev_proof = prev_block['proof']
    proof = blockchain.proof_of_work(prev_proof)
    previous_hash = blockchain.hassher(prev_block)
    blockchain.add_transactions(sender = node_address, receiver = 'Dennis', amount = 1)
    block = blockchain.create_block(proof, previous_hash) 
    response = {'message' : 'Congrats block mined',
                'index':block['index'],
                'proof': block['proof'],
                'previous_hash':block['prev_hash'],
                'transactions':block['transactions']
                  }
    return response
print(mine_block())


s.start()

