from ticTacToe import printGameBoard


def test_GameBoardshouldBePrintedCorrectly(capfd):
    printGameBoard()
    out, err = capfd.readouterr()
    correctBoard = """\n+---+---+---+\n| 1 | 2 | 3 |\n+---+---+---+\n| 4 | 5 | 6 |\n+---+---+---+\n| 7 | 8 | 9 |\n+---+---+---+\n"""
    assert out == correctBoard
    