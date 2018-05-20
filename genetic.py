from algorithm import min_max
from game import getNewBoard, resetBoard, getComputerMove, makeMove
from prototype import getScoreOfPlayerTree
from interpreter import parse_tree

board = getNewBoard()
resetBoard(board)

firstMove = getComputerMove(board, 'O')
makeMove(board, 'O', firstMove[0], firstMove[1])

player = 'X'

evalScoreOfPlayer = parse_tree(0 , getScoreOfPlayerTree)

min_max(board, player, 4, evalScoreOfPlayer)

