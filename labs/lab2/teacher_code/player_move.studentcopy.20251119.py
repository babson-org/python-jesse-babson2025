<<<<<<< HEAD
def player_move(board: list[int], score: dict[str, int]):
    """
    Prompts the player to choose a valid move.
    """
    prompt = 'Select an empty cell (1–9): '
    while True:
        try:
            move = int(input(prompt))
            if move < 1 or move > 9 or abs(board[move - 1]) == abs(score['player']):
                raise ValueError
            break
        except ValueError:
            prompt = 'Invalid. Try again with an empty cell index (1–9): '
    
    board[move - 1] = score['player']    
=======
def player_move(board: list[int], score: dict[str, int]):
    """
    Prompts the player to choose a valid move.
    """
    prompt = 'Select an empty cell (1–9): '
    while True:
        try:
            move = int(input(prompt))
            if move < 1 or move > 9 or abs(board[move - 1]) == abs(score['player']):
                raise ValueError
            break
        except ValueError:
            prompt = 'Invalid. Try again with an empty cell index (1–9): '
    
    board[move - 1] = score['player']    
>>>>>>> 071ea7f10dd3616d394fdce02072ea5f94b2082f
