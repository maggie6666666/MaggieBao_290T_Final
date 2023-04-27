import random

possibleNumbers = [1,2,3,4,5,6,7,8,9]
gameBoard = [[1,2,3], [4,5,6], [7,8,9]]
ROWS = 3
COLS = 3

def printGameBoard(gameBoard):
  for x in range(ROWS):
    print("\n+---+---+---+")
    print("|", end="")
    for y in range(COLS):
      print("", gameBoard[x][y], end=" |")
  print("\n+---+---+---+")

  

