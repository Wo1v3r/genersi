from constants import *
from game import getScoreOfPlayer, getScoreOfBoard

functions = {
  IF:  lambda values :  values[1] if values[0] else values[2],
  EQUALS:  lambda values : 1 if values[0] == values[1] else 0,
  GREATER:  lambda values : 1 if values[0] > values[1] else 0,
  # LOWER:  lambda values : 1 if values[0] < values[1] else 0,
  MINUS: lambda values : values[0] - values[1],
  PLUS: lambda values: values[0] + values[1],
  MUL: lambda values: values[0] * values[1],
  DIV: lambda values: values[0] // values[1] if values[1] != 0 else 0
}

arguments = lambda name : 3 if name == IF else 2

terminals = {
  PLAYER_X: lambda board, player: PLAYER_X,
  PLAYER_O: lambda board, player: PLAYER_O,
  PLAYER :lambda board, player: player,

  
  PLAYER_O_SCORE: lambda board, player:  getScoreOfPlayer(board, PLAYER_O),
  PLAYER_X_SCORE: lambda board, player : getScoreOfPlayer(board, PLAYER_X),
  EMPTY: lambda board, player: getScoreOfBoard(board)[' '],
  PLAYER_SCORE: lambda board, player : getScoreOfPlayer(board,player),
}

numbers = [ str(x) for x in range(64)]
