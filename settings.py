from constants import *
from game import getScoreOfBoard
  
functions = {
  IF:  lambda values : values[THEN] if values[CONDITION] else values[ELSE],
  EQUALS:  lambda values : list(values.values())[0] == list(values.values())[1],
  MINUS: lambda values : list(values.values())[0] - list(values.values())[1],
  CONDITION: lambda values:  list(values.values())[0],
  THEN: lambda values : list(values.values())[0],
  ELSE:  lambda values : list(values.values())[0],
}

terminals = {
  PLAYER_X: lambda board, player: PLAYER_X,
  PLAYER_O: lambda board, player: PLAYER_O,
  PLAYER :lambda board, player: player,
  PLAYER_O_SCORE: lambda board, player:  getScoreOfBoard(board)[PLAYER_O],
  PLAYER_X_SCORE: lambda board, player : getScoreOfBoard(board)[PLAYER_X]
}
