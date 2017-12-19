
def determine_winner(GameState:GameState):
    if winner(GameState) == RED:
        return 'Red player wins'
    elif winner(GameState) == YELLOW:
        return 'Yellow player wins'