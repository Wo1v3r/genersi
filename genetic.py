from algorithm import min_max
from game import getNewBoard, resetBoard, getComputerMove, makeMove, getScoreOfPlayer
from constants import *
from individual import IndividualFactory


board = getNewBoard()
resetBoard(board)

firstMove = getComputerMove(board, PLAYER_O)

makeMove(board, PLAYER_O, firstMove[0], firstMove[1])


individual = IndividualFactory.prototype()
min_max(board, PLAYER_X, 2,  individual.eval)