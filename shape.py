game_positions = {
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9'
    }


def get_board():
    """
    Prints the game board
    """
    game_shape = f"""
          {game_positions[1]} | {game_positions[2]} | {game_positions[3]} 
        ------------
          {game_positions[4]} | {game_positions[5]} | {game_positions[6]}  
        ------------
          {game_positions[7]} | {game_positions[8]} | {game_positions[9]}  
        """

    print(game_shape)
