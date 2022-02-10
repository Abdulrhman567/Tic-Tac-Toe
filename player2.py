from shape import game_positions


class PlayerO:
    def __init__(self):
        self.player_char = 'O'
        self.pick_position = 0
        self.score = 0

    def player_move(self):
        """
        player will make a move by choosing a number and that number will be checked if it's on the bored or not and if
        not the move will be considered otherwise it will recall it self
        """
        self.pick_position = int(input(f"Please player 2 make a move (1-9): "))
        if game_positions[self.pick_position] == 'X' or game_positions[self.pick_position] == 'O':
            print("This position is already full please try again!")
            self.player_move()
        else:
            game_positions[self.pick_position] = self.player_char

    def check_game_on_o(self):
        """
        Checks if player 2 has won or not and if the player won it increases the score by 1 and returns True
        """
        if ((game_positions[1] == self.player_char and game_positions[2] == self.player_char and game_positions[3] == self.player_char) or
                (game_positions[1] == self.player_char and game_positions[4] == self.player_char and game_positions[7] == self.player_char) or
                (game_positions[1] == self.player_char and game_positions[5] == self.player_char and game_positions[9] == self.player_char) or
                (game_positions[2] == self.player_char and game_positions[5] == self.player_char and game_positions[8] == self.player_char) or
                (game_positions[3] == self.player_char and game_positions[5] == self.player_char and game_positions[7] == self.player_char) or
                (game_positions[3] == self.player_char and game_positions[6] == self.player_char and game_positions[9] == self.player_char) or
                (game_positions[4] == self.player_char and game_positions[5] == self.player_char and game_positions[6] == self.player_char) or
                (game_positions[7] == self.player_char and game_positions[8] == self.player_char and game_positions[9] == self.player_char)):
            self.score += 1
            return True
        return False
