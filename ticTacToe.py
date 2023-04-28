# Understands the rules of TicTacToe
import random

POSSIBLE_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
VALID_MARK = ['X', 'O']
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
    if player_mark in VALID_MARK:
        for row in game_board:
            for i, tile in enumerate(row):
                if tile == tile_number:
                    row[i] = player_mark
    else:
        print("Invalid Mark. Please try again.")

def get_player_choice(possible_numbers):
    """Gets a valid tile choice from the player."""
    player_choice = None
    attempts = 0
    while player_choice not in possible_numbers and attempts < 3:
        player_choice = int(input("Choose a tile (1-9): "))
        if player_choice not in possible_numbers:
            print("Invalid choice. Please try again.")
            attempts += 1
    if attempts == 3:
        raise ValueError("Too many invalid choices.")
    return player_choice

def check_for_winner(game_board):
    """Checks if there is a winner, and returns their mark if there is."""
    rows = (
        game_board
        + [list(x) for x in zip(*game_board)]
        + [[game_board[i][i] for i in range(3)], [game_board[i][2 - i] for i in range(3)]]
    )
    for row in rows:
        if row == ["X", "X", "X"]:
            return "X"
        elif row == ["O", "O", "O"]:
            return "O"
    return None

def play():
    pass