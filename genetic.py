from algorithm import *
from game import *


board = getNewBoard()

resetBoard(board)

firstMove = getComputerMove(board, 'O')
makeMove(board, 'O', firstMove[0], firstMove[1])

player = 'X'


min_max(board, player, 7, getScoreOfPlayer)