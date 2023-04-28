from ticTacToe import *
from io import StringIO
from unittest.mock import patch
import pytest

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

def test_markAnEmptyTileWithUnknownMarkShouldNotUpdateBoard(capfd):
    game_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mark_tile(game_board, 3, '*')
    out, err = capfd.readouterr()
    CorrectMessage = "Invalid Mark. Please try again.\n"
    assert game_board == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert out == CorrectMessage

def test_markAnEmptyTileWithUnknownMarkShouldPromptMessage(capfd):
    game_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mark_tile(game_board, 3, '*')
    out, err = capfd.readouterr()
    CorrectMessage = "Invalid Mark. Please try again.\n"
    assert out == CorrectMessage

def test_markInvalidTileShouldNotUpdateBoard():
    game_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mark_tile(game_board, 10, 'X')
    assert game_board == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


