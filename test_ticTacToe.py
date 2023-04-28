from ticTacToe import *
from io import StringIO
from unittest.mock import patch

def test_InitialGameBoardshouldBePrintedCorrectly(capfd):
    inital_gameBoard = [[1,2,3], [4,5,6], [7,8,9]]
    print_game_board(inital_gameBoard)
    out, err = capfd.readouterr()
    correctBoard = """\n+---+---+---+\n| 1 | 2 | 3 |\n+---+---+---+\n| 4 | 5 | 6 |\n+---+---+---+\n| 7 | 8 | 9 |\n+---+---+---+\n"""
    assert out == correctBoard

def test_markAnEmptyTileWithXShouldUpdateBoard():
    game_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mark_tile(game_board, 5, 'X')
    assert game_board == [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]

def test_markAnEmptyTileWithOShouldUpdateBoard():
    game_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mark_tile(game_board, 2, 'O')
    assert game_board == [[1, 'O', 3], [4, 5, 6], [7, 8, 9]]
