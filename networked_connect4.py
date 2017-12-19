#Spencer Wittrock 84023369 & Emma Lisowski 26903080

from sockets_setup import *
from connectfour import *
from console_only import *

def server_game(connection:socket):
    '''controls the logic for running a server game after the connection has been established'''
    GameState = new_game()
    game_board_gui(GameState)

    while True:
        try:
            choice = input('drop, or pop?')
            if choice == 'drop' or choice == 'pop':
                column_choice = int(input('Which column? (1-{})'.format(BOARD_COLUMNS)))-1
            else:
                raise "error"


            GameState = command_choice(choice, column_choice, GameState)

            if determine_winner(GameState) != None:
                print(determine_winner(GameState))
                break

            connection.output.write(choice.upper() + ' ' + str(column_choice + 1) + '\r\n')
            connection.output.flush()

            x = connection.input.readline()
            command = connection.input.readline()
            z = connection.input.readline()

            things = command.split()
            ai_choice = things[0]
            ai_column_choice = int(things[1])-1

            print()
            print("AI turn")
            print()

            GameState = command_choice(ai_choice, ai_column_choice, GameState)

            if determine_winner(GameState) != None:
                print(determine_winner(GameState))
                break

        except:
            print('input error - connection closed')
            break
      

def ui_connect()-> None:
    '''prompts the user for input to connect to a server'''
    try:
        host = input('Enter either an IP address or the host name: ')
        port = int(input('Enter the port number: '))
        user_name = input('Enter a username (no whitespaces): ')

        if ' ' in user_name:
            raise 'error'

        connection = connect(host, port)
        AI_setup(connection, user_name)

        print('Connected')
    except:
        print('Could not connect to the specified server')
    try:
        server_game(connection)
    except:
        print('could not start game')
    
if __name__ == "__main__":
    ui_connect()

 
