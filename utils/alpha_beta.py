import copy

from game.controller import *
from settings.constants import *

toggle_player = { PLAYER_X : PLAYER_O , PLAYER_O: PLAYER_X}

def moveBoard(board,move,player):
  board = copy.deepcopy(board)
  makeMove(board, player, move[0], move[1])
  return board


def alphaBeta(board, player, depth, item, maximizingPlayer, alpha, beta):
  moves = getValidMoves(board,player)

  if depth == 0 or len(moves) == 0:
    return item.eval(board,player)

  v = None

  if maximizingPlayer:
    v = -float('inf')

    for move in moves:
      new_board = moveBoard(board, move, player)
      v = max(v, alphaBeta(new_board,toggle_player[player], depth - 1, item, False, alpha, beta))
      alpha = max(alpha, v)

      if beta <= alpha:
        break

  else:
    v = float('inf') 

    for move in moves:
      new_board = moveBoard(board, move, player)
      v = min(v, alphaBeta(new_board,toggle_player[player], depth - 1, item , True, alpha, beta))
      beta = min(beta, v)

      if beta <= alpha:
        break

  return v


def bestMove(board, player, depth, item):
  moves = getValidMoves(board,player)
  best_move = None
  best_score = -float('inf')
  

  for move in moves:
    new_board = moveBoard(board, move, player)
    move_score = alphaBeta(new_board, toggle_player[player], depth,item , False, -float('inf'), float('inf'))
    best_move = move if move_score > best_score else best_move
    best_score = move_score if move_score > best_score else best_score
    

  return best_move


def memoize(f):
  cache = {}

  def memoized(board, player, depth, item):
    
    hashed = str((board, player, depth, item.id))

    if hashed not in cache:
      cache[hashed] = f(board, player, depth, item)
    return cache[hashed]

  return memoized

evaluateBoard = memoize(bestMove)