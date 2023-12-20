#!/usr/bin/env python3
import socket
import threading
import pickle


class server:
    def __init__(self):
        self.known_port = 50002
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverip = socket.gethostbyname(socket.gethostname())
        self.sock.bind(('0.0.0.0', 55555))
        self.addr = " "
        self.clients = []
    def handle_client(self, addr):
        connected = True
        print(f'{self.serverip} server ip.')
        print(f'{addr} connected.')
        self.clients.append(addr)
        print(self.clients)
        
        if len(self.clients) >= 2:
            for client in self.clients:
                data = pickle.dumps(self.clients)

                c1_addr, c1_port = client
                print(f'C1 address{c1_addr}, port {c1_port}')
                self.sock.sendto(data, client)
                #self.sock.sendto('{} {} {}'.format(c1_addr, c1_port, self.known_port).encode(), self.clients)
            '''
            c1 = clients.pop()
            c1_addr, c1_port = c1
            c2 = clients.pop()
            c2_addr, c2_port = c2

            sock.sendto('{} {} {}'.format(c1_addr, c1_port, known_port).encode(), c2)
            sock.sendto('{} {} {}'.format(c2_addr, c2_port, known_port).encode(), c1)
            sock.sendto(clients, address)
            print('got 2 clients, sending details to each')
            break
            '''
        pass
    def starter(self):
        while True:
            print(f"Waiting for nodes...")
            data, addr = self.sock.recvfrom(1028)
            print('connection from: {}'.format(addr[0]))
            thread = threading.Thread(target=self.handle_client, args=(addr,))
            print(f'the addr {addr} the data {data}.')
            thread.start()

s = server()
s.starter()

    