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

# This edge case will alsp be taken care of by play() function
def test_markAnEmptyTileWithUnknownMarkShouldPromptMessage(capfd):
    game_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mark_tile(game_board, 3, '*')
    out, err = capfd.readouterr()
    CorrectMessage = "Invalid Mark. Please try again.\n"
    assert out == CorrectMessage

# This edge case will alsp be taken care of by get_player_choice() function
def test_markInvalidTileShouldNotUpdateBoard():
    game_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mark_tile(game_board, 10, 'X')
    assert game_board == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def test_validInputShouldBeProcessed():
    with patch('sys.stdin', StringIO('3\n')):
        assert get_player_choice([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 3


def test_threeInvalidInputShouldPromptErrorMessage():
    with patch('sys.stdin', StringIO('0\n10\n11\n')):
        try:
            get_player_choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
        except ValueError as e:
            assert str(e) == "Too many invalid choices."

def test_lessThanThreeInvalidInputCanBeCorrected():
    with patch('sys.stdin', StringIO('0\n2\n')):
        assert get_player_choice([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2

def test_aVerticalWinningRowShouldBeIdentified():
    game_board = [['O', 'X', 'X'], ['X', 'O', 'X'], ['O', 'O', 'X']]
    assert check_for_winner(game_board) == 'X'

def test_aHorizontalWinningRowShouldBeIdentified():
    game_board = [['O', 'O', 'O'], ['X', 'X', 'O'], ['O', 'X', 'X']]
    assert check_for_winner(game_board) == 'O'

def test_aDiagonalWinningRowShouldBeIdentified():
    game_board = [['O', 'O', 'X'], ['X', 'O', 'X'], ['X', 'X', 'O']]
    assert check_for_winner(game_board) == 'O'

def test_shouldReturnXifXhasWon():
    inputs = ['1', '5', '2', '6', '3']
    input_mock = StringIO('\n'.join(inputs))
    with patch('sys.stdin', input_mock):
        output_mock = StringIO()
        with patch('sys.stdout', output_mock):
            result = play()
            assert result == 'X'