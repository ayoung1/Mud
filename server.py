#! /usr/bin/env python

import socket
import sys
from sneakymud import GameEngine
from thread import *

HOST = '0.0.0.0'
PORT = 5001

class Server(object):
    def __init__(self, host=HOST, port=PORT):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port

    def connect(self):
        try:
            self.socket.bind((self.host, self.port))
            self.socket.listen(10)
            while True:
                conn, addr = self.socket.accept()
                start_new_thread(self._client_thread, (conn,))
        except Exception as e:
            print('Something went wrong : {}'.format(e))
        finally:
            self.socket.close()

    def _client_thread(self, conn):
        gameInstance = GameEngine()
        conn.send(gameInstance.display() + "\n")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            if gameInstance.getPlayerInput(data) == 'EXIT':
                break
            conn.sendall(gameInstance.display() + "\n")
        conn.close()

if __name__ == "__main__":
    Server().connect()
