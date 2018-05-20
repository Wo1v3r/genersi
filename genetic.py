from algorithm import min_max
from game import getNewBoard, resetBoard, getComputerMove, makeMove, getScoreOfPlayer
from prototype import getScoreOfPlayerTree
from interpreter import parse_tree
from constants import *


board = getNewBoard()
resetBoard(board)

firstMove = getComputerMove(board, PLAYER_O)
makeMove(board, PLAYER_O, firstMove[0], firstMove[1])

evalScoreOfPlayer = parse_tree(0 , getScoreOfPlayerTree)

min_max(board, PLAYER_X, 4,  evalScoreOfPlayer)
