#Spencer Wittrock 84023369 & Emma Lisowski 26903080
from collections import namedtuple
import socket

Connect4Connection = namedtuple(
    'Connect4Connection',
    ['socket', 'input', 'output'])

def connect(host: str, port: int) -> Connect4Connection:
    '''handles input to connect to a socket'''
    connect4_socket = socket.socket()
    
    connect4_socket.connect((host, port))

    connect4_input = connect4_socket.makefile('r')
    connect4_output = connect4_socket.makefile('w')

    return Connect4Connection(
        socket = connect4_socket,
        input = connect4_input,
        output = connect4_output)



def AI_setup(connection:'namedtuple', user_name):
    '''sends the info to the server for establishing an AI game'''
    connection.output.write('I32CFSP_HELLO ' + user_name + '\r\n')
    connection.output.flush()
    print(connection.input.readline()[:-1])
    connection.output.write('AI_GAME \r\n')
    connection.output.flush()
    print(connection.input.readline()[:-1])



        
        





    
    
    
