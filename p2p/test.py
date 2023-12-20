#!/usr/bin/env python3
import requests
import json

receive = requests.get('http://127.0.0.1:8000/blockchaindata')
receive = receive.json()
print(f'Reveived: {receive["numb"]}')