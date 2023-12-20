#!/usr/bin/env python3
import datetime
import hashlib
import json
import requests
from uuid import uuid4
from urllib.parse import urlparse
from flask import Flask, jsonify, request


class Blockchain:
    #Blockchain Build
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, prev_hash="0", thedata={})
        self.nodes = set()
    
    def create_block(self, proof, prev_hash, thedata):
        block = {'index':len(self.chain)+1, 
                 'timestamp':str(datetime.datetime.now()),
                 'proof':proof,
                 'prev_hash':prev_hash,
                 'thedata':thedata}
        self.transactions = []
        self.chain.append(block)
        return block
    
    def get_last_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, prev_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            #problem definition for the miners.
            hash_orp = hashlib.sha256(str(new_proof**2 - prev_proof**2).encode()).hexdigest()#le problem()
            if hash_orp[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    def hassher(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        
        prev_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['prev_hash'] != self.hassher(prev_block):
                return False
            prev_proof = prev_block['proof']
            proof = block['proof']
            hash_orp = hashlib.sha256(str(proof**2 - prev_proof**2).encode()).hexdigest()
            if hash_orp != '0000':
                return False
            prev_block = block
            block_index += 1
        return True
    #turn to crypto
    def add_node(self, address):
        for addres in address:
            print(f'pre-parsed url {addres}')
            parsed_url = urlparse(addres[0])
            print(f'To be Added {parsed_url}')
            self.nodes.add(parsed_url.path)
            print(f'The nodes {self.nodes}')
            pass
        pass
    	
    def replace_chain(self):
        network = self.nodes
        longest_chain = None
        max_length = len(self.chain)
        for node in network:
            response = requests.get(f'http://{ip}:{port}/get_chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                if length > max_length and self.is_chain_valid(chain):
                    max_length = length
                    longest_chain = chain
        if longest_chain:
            self.chain = longest_chain
            return True
        return False
        
'''   
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
    return jsonify(response), 200


def get_chain():
    response = {'chain':blockchain.chain,
                'length':len(blockchain.chain)}
    return jsonify(response), 200

def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': 'Chain is valid'} 
    else:
        response = {'message':'chain is invalid'}
    
    return jsonify(response), 200
def add_transaction():
    json = request.get_json() 
    transaction_keys = ['sender, receiver, amount']
    if not all (key in json for key in transaction_keys):
        return 'some elemnets of the transactions missing', 400
    index = blockchain.add_transaction(json['sender'], json['receiver'], json['amount'])
    responce = {'message':f'This transaction will be added to the block {index}'}
    return jsonify(responce), 201 
def connect_node(thenodes):
    json = request.get_json()
    nodes = json.get('nodes')
    if nodes is None:
        return 'No Nodes', 400
    for node in nodes:
        blockchain.add_node(node)
        responce = blockchain.nodes #{'message':'All nodes connected, total nodes':'Total nodes':list(blockchain.nodes)}
        return jsonify(responce), 201
def replace_cahin():
    is_chain_replaced = blockchain.replace_chain()
    if is_chain_replaced:
        response = {'message': 'Chain is replace', 'New chain':blockchain.chain} 
    else:
        response = blockchain.chain #{'message':'chain is the longest':'Longest chain': blockcahin.chain}
    
    return jsonify(response), 200
'''