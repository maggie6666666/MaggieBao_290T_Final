import random

POSSIBLE_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ROWS = 3
COLS = 3

def print_game_board(game_board):
    for x in range(ROWS):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(COLS):
            print("", game_board[x][y], end=" |")
    print("\n+---+---+---+")
    

def mark_tile(game_board, tile_number, player_mark):
    """Updates the board state with the player's tile choice."""
    for row in game_board:
        for i, tile in enumerate(row):
            if tile == tile_number:
                row[i] = player_mark
