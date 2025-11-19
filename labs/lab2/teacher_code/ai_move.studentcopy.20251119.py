<<<<<<< HEAD
def ai_move(board: list[int]):
    """
    Simple AI that selects the first available cell.
    """
    for move, cell in enumerate(board):
        if abs(cell) != 10:
            return move
           

'''
for cell in board:
    if abs(cell) != 10: boardreturn mark
return None
'''
=======
def ai_move(board: list[int]):
    """
    Simple AI that selects the first available cell.
    """
    for move, cell in enumerate(board):
        if abs(cell) != 10:
            return move
           

'''
for cell in board:
    if abs(cell) != 10: boardreturn mark
return None
'''
>>>>>>> 071ea7f10dd3616d394fdce02072ea5f94b2082f
