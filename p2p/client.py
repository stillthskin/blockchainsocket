#!/usr/bin/env python3
import socket
import sys
import threading
import pickle
import requests
from blockchain import Blockchain

class Client:
    
    def __init__(self):
        self.rendezvous = ('127.0.0.1', 55555)
        # connect to rendezvous
        print('connecting to rendezvous server')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('0.0.0.0', 50001))
        self.sock.sendto(b'0', self.rendezvous)
    def start(self):
        while True:
            print("waiting...")
            self.sock.sendto(b'0', self.rendezvous)
            data = pickle.loads(self.sock.recv(1024))
            #data = self.sock.recv(1024).decode()
            print(f'Data received is: {data}')
            break
        
            #b.add_node(address)
            '''
            if data.strip() == 'ready':
                print('checked in with server, waiting')
                break
            '''
        return data
    def start_p2p(self):
        self.b.add_node()
        pass
    '''
    data = sock.recv(1024).decode()
    ip, sport, dport = data.split(' ')
    sport = int(sport)
    dport = int(dport)

    print('\ngot peer')
    print('  ip:          {}'.format(ip))
    print('  source port: {}'.format(sport))
    print('  dest port:   {}\n'.format(dport))

    # punch hole
    # equiv: echo 'punch hole' | nc -u -p 50001 x.x.x.x 50002
    print('punching hole')

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', sport))
    sock.sendto(b'0', (ip, dport))
    """
    clientSocket.send(b"GET / HTTP/1.1\r\nHost:localhost\r\n\r\n")
    response = clientSocket.recv(4096)
    print(response.decode())

    # second GET request
    clientSocket.send(b"GET /file.txt HTTP/1.1\r\nHost:localhost\r\n\r\n")
    response = clientSocket.recv(4096)
    print(response.decode())

    """
    print('ready to exchange messages\n')

    # listen for
    # equiv: nc -u -l 50001
    def listen():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('0.0.0.0', sport))

        while True:
            data = sock.recv(1024)
            print('\rpeer: {}\n> '.format(data.decode()), end='')

    listener = threading.Thread(target=listen, daemon=True);
    listener.start()

    # send messages
    # equiv: echo 'xxx' | nc -u -p 50002 x.x.x.x 50001
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', dport))

    while True:
        msg = input('> ')
        sock.sendto(msg.encode(), (ip, sport))
    '''
c = Client()
nodelist = c.start()
blockchain = Blockchain()
blockchain.add_node(nodelist)
print("the nnnnodes")
print(blockchain.nodes)
def mine_block():
    prev_block = blockchain.get_last_block()
    prev_proof = prev_block['proof']
    thechain = blockchain.chain
    proof = blockchain.proof_of_work(prev_proof)
    previous_hash = blockchain.hassher(prev_block)
    thedata = requests.get('http://192.168.100.14:8000/blockchaindata')
    thedata = thedata.json()
    block = blockchain.create_block(proof, previous_hash, thedata) 
    print(thechain)
    context = {'message' : 'Congrats block mined',
                    'index':block['index'],
                    'proof': block['proof'],
                    'previous_hash':block['prev_hash'],
                    'data':thedata,
                    'block':block,
                    'chain':thechain
                      }
    return context
def replace_chin():
    is_chain_replaced = blockchain.replace_chain()
    if is_chain_replaced:
        response = {'message': 'Chain is replace', 'New chain':blockchain.chain} 
    else:
        response = {'message':'chain is the longest', 'Longest chain': blockchain.chain}
    
    return response
print(mine_block())
print(replace_chin())
