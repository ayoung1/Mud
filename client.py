#! /usr/bin/env python

import socket
import select
import string
import sys

HOST = '54.201.125.142'
PORT = 5001

class Client(object):
    def __init__(self, host=HOST, port=PORT):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(2)
        self.host = host
        self.port = port

    def connect(self):
        try:
            self.socket.connect((self.host, self.port))
            while True:
                socket_list = [sys.stdin, self.socket]
                read_sockets, write_sockets, err_sockets = select.select(socket_list, [], [])
                for sock in read_sockets:
                    if sock == self.socket:
                        data = sock.recv(4096)
                        if not data:
                            print("Connection Closed")
                            raise Exception
                        else:
                            sys.stdout.write(data)
                    else:
                        msg = sys.stdin.readline()
                        self.socket.send(msg.rstrip())
        except Exception as e:
            print("Something went wrong")
        finally:
            self.socket.close()

if __name__ == '__main__':
    Client().connect()
