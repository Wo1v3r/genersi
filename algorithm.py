from game import *
from constants import *
import copy

toggle_player = { PLAYER_X : PLAYER_O , PLAYER_O: PLAYER_X}

def moveBoard(board,move,player):
  board = copy.deepcopy(board)
  makeMove(board, player, move[0], move[1])
  return board


evalFunc = None

def min_max(board, player, depth, f):
  global evalFunc
  evalFunc = f

  move_scores = []

  moves = getValidMoves(board,player)

  for move in moves:
    new_board = moveBoard(board, move, player)
    move_scores.append(min_val(new_board, depth, toggle_player[player]))

  index = 0

  for move in moves:
    print('MM for: ' + str(move) + ' '+ str(move_scores[index]))
    index = index + 1

  return max(move_scores)

def min_val(board, depth, player):
  depth = depth - 1
  moves = getValidMoves(board,player)

  move_scores = []

  #this is incorrect
  if depth < 0  or len(moves) == 0:
    return evalFunc(board,player)
  
  for move in moves:
    new_board = moveBoard(board, move, player)
    move_scores.append(max_val(new_board, depth, toggle_player[player]))

  return min(move_scores)

def max_val(board, depth, player):
  depth = depth - 1
  
  moves = getValidMoves(board,player)
  move_scores = []
  

  #this is incorrect
  if depth < 0 or len(moves) == 0:
    return evalFunc(board,player)

  for move in moves:
    board = moveBoard(board, move, player)
    move_scores.append(min_val(board, depth,toggle_player[player]))

  return max(move_scores)