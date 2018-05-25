from game import *
from constants import *
import copy

toggle_player = { PLAYER_X : PLAYER_O , PLAYER_O: PLAYER_X}

def moveBoard(board,move,player):
  board = copy.deepcopy(board)
  makeMove(board, player, move[0], move[1])
  return board


def min_max(board, player, depth, item):
  moves = getValidMoves(board,player)

  if len(moves)  == 0:
    return None

  bestMove = moves[0]
  bestMoveScore = -1000

  for move in moves:
    new_board = moveBoard(board, move, player)
    moveScore = min_val(new_board, depth, toggle_player[player], item)
    bestMove = move if moveScore > bestMoveScore else bestMove
    bestMoveScore = moveScore if moveScore > bestMoveScore else bestMoveScore

  return bestMove

def memoize(f):
  cache = {}

  def memoized(board,depth, player, item):
    
    hashed = str((board,depth,player,item.id))

    if hashed not in cache:
      cache[hashed] = f(board,depth,player,item)
    return cache[hashed]

  return memoized

evaluateBoard = memoize(min_max)

def min_val(board, depth, player, item):
  depth = depth - 1
  moves = getValidMoves(board,player)

  move_scores = []

  #this is incorrect
  if depth < 0  or len(moves) == 0:
    return item.eval(board,player)
  
  for move in moves:
    new_board = moveBoard(board, move, player)
    move_scores.append(max_val(new_board, depth, toggle_player[player], item))

  return min(move_scores)

def max_val(board, depth, player, item):
  depth = depth - 1
  
  moves = getValidMoves(board,player)
  move_scores = []
  

  #this is incorrect
  if depth < 0 or len(moves) == 0:
    return item.eval(board,player)

  for move in moves:
    board = moveBoard(board, move, player)
    move_scores.append(min_val(board, depth,toggle_player[player],item))

  return max(move_scores)