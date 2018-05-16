from game import *
from human import *
import copy

inf = float("inf")
toggle_player = { 'X' : 'O' , 'O': 'X'}



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
    move_scores.append(memoized_min(new_board, depth, toggle_player[player]))

  index = 0

  for move in moves:
    print('MM for: ' + str(move) + ' '+ str(move_scores[index]))
    index = index + 1

  return max(move_scores)



def memoize(f):
  results = {}

  def memoized(board,depth,player):
    if (str(board),depth,player) not in results:
      results[(str(board),depth,player)] = f(board,depth,player)

    return results[(str(board),depth,player)]

  return memoized


def min_val(board, depth, player):
  depth = depth - 1
  moves = getValidMoves(board,player)

  move_scores = []

  #this is incorrect
  if depth < 0  or len(moves) == 0:
    return evalFunc(board,player)

  
  for move in moves:
    new_board = moveBoard(board, move, player)
    move_scores.append(memoized_max(new_board, depth, toggle_player[player]))

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
    move_scores.append(memoized_min(board, depth,toggle_player[player]))

  return max(move_scores)

memoized_min = memoize(min_val)
memoized_max = memoize(max_val)