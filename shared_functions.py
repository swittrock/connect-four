#Spencer Wittrock 84023369 & Emma Lisowski 26903080
from connectfour import *


def game_board_gui(GameState) ->str:
    zero_list = []
    for x in range(BOARD_COLUMNS):
        print(x+1,end=' ')
    print()
    for column in GameState.board:
        column_list = []
        for row in column:
            if row == 0:
                column_list.append('.')
            elif row == 1:
                column_list.append('R')
            elif row == 2:
                column_list.append('Y')
        zero_list.append(column_list)
    for column in zip(*zero_list):
        print(*column)


def command_choice(choice: str, column_choice: int, GameState: 'GameState'):
    if choice == 'drop' or choice == 'DROP':
        game_board_gui(drop(GameState, column_choice))
        return drop(GameState, column_choice)

    elif choice == 'pop' or choice == 'POP':
        game_board_gui(pop(GameState, column_choice))
        return pop(GameState, column_choice)

def run_game():
    new_game()
    game_board_gui(new_game())
    GameState = new_game()
    while True:
        try:
            print('Player', GameState.turn)
            choice = input('drop, or pop? ')
            if choice == 'drop' or choice == 'pop':
                column_choice = int(input('Which column? (1-{})'.format(BOARD_COLUMNS))) - 1
            else:
                raise "error"
            # print(command_choice(choice, column_choice, GameState))
            GameState = command_choice(choice, column_choice, GameState)

            if winner(GameState) == RED:
                print('Red player wins')
                break
            elif winner(GameState) == YELLOW:
                print('Yellow player wins')
                break

        except:
            print('ERROR')

def determine_winner(GameState:GameState):
    if winner(GameState) == RED:
        return 'Red player wins'
    elif winner(GameState) == YELLOW:
        return 'Yellow player wins'