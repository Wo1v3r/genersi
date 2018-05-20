from algorithm import *
from game import *
from prototype import *
from human import *

board = getNewBoard()
resetBoard(board)

firstMove = getComputerMove(board, 'O')
makeMove(board, 'O', firstMove[0], firstMove[1])

player = 'X'
count = 0


parsed_tree = parse_tree(0 , getScoreOfPlayerTree)

def evaluate(board,player):
  value = parsed_tree(board,player)
  return value

min_max(board, player, 4, evaluate)

