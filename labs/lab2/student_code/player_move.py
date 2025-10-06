    
def player_move(board: list[int], score: dict[str, int]):
    """
        Prompts the player to choose a valid move.
        Remember score is a dictionary from play_game()
        It has two keys 'player' and 'ai' associated values
        are 10 and -10 depending on who goes first.
    """
   #### I placed my prompt inside the while loop to make sure user doesn't crash system ####
    while True:
        try:
            # TODO: Convert input to integer
            prompt = int(input("Select an empty cell (1-9): "))
            
            # TODO: Validate move is in range and not taken
            # for the range
            if prompt < 1 or prompt > 9:
                print("Outside of range")
                continue
            
            # Checking if cell is empty
            ### Used prompt-1 to get the right indicies 
            ## 0 is the first cell, which corresponds to 1
            if board[prompt - 1] in [10,-10]:
                print("This cell is already taken please chose another")
                continue
            
            ### Assigning to score['player']
            board[prompt - 1] = score['player']
            break
        
        except ValueError:
            prompt = "Invalid input. Try again (1-9): "
            
    # TODO: Assign score['player'] to the selected cell on the board
    # HINT: remember the board moves are 1 - 9 but the board indices are
    # 0 - 8

