from shape import get_board, game_positions
from player1 import PlayerX
from player2 import PlayerO
import os


# To clear the console
def clear_console():
    os.system('cls')


# Game functionality
def game():
    get_board()
    game_on = True
    while game_on:
        player_1.player_move()
        all_moves.append(player_1.pick_position)
        get_board()
        if player_1.check_game_on_x():
            print("Player 1 won, Congrats!")
            game_on = False
        elif len(all_moves) == 9:
            print("It's a Tie!")
            game_on = False
        else:
            player_2.player_move()
            all_moves.append(player_1.pick_position)
            get_board()

        if player_2.check_game_on_o():
            print("Player 2 won, Congrats!")
            game_on = False

    if input("Do you want to play again?(y/n): ").lower() == 'y':
        for key in range(1, 10):
            game_positions[key] = str(key)
        all_moves.clear()
        clear_console()
        game()


if __name__ == '__main__':
    # Setting Players
    player_1 = PlayerX()
    player_2 = PlayerO()

    all_moves = []

    game()

    # Setting players scores
    player_1_score = player_1.score
    player_2_score = player_2.score

    print(f"Player 1 score: {player_1_score}, Player 2 score: {player_2_score}")
