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
    player_choice = None
    while player_choice not in possible_numbers:
        player_choice = int(input("Choose a tile (1-9): "))
        if player_choice not in possible_numbers:
            print("Invalid choice. Please try again.")
    return player_choice

def check_for_winner(game_board):
    pass

def play():
    pass