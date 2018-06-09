from utils.alpha_beta import evaluateBoard
from game.controller import (
    getNewBoard,
    resetBoard,
    getComputerMove,
    makeMove,
    getScoreOfPlayer,
    winner,
    gameOver
)

from settings.constants import PLAYER_X, PLAYER_O
from settings.variables import MAX_DEPTH

class Game:
 
 def __init__(self , player, opponent):
  self.playerScore = 0
  
  self.player = player
  self.opponent = opponent

 def match(self, player1, player2):
  board = getNewBoard()
  resetBoard(board)
  
  while not gameOver(board):
    step = evaluateBoard(board, PLAYER_X, MAX_DEPTH,  player1)

    if step is not None:
      makeMove(board, PLAYER_X, step[0], step[1])

    step = evaluateBoard(board, PLAYER_O, MAX_DEPTH,  player2)

    if step is not None: 
      makeMove(board, PLAYER_O, step[0], step[1])

  return winner(board)


 def score(self, player, winner):
  if winner == 'TIE':
    self.playerScore += 1
  elif winner == player:
    self.playerScore += 2
 
 def play(self):
  winner = self.match(self.player, self.opponent)
  self.score('X', winner)
  
  winner = self.match(self.opponent, self.player)
  self.score('O', winner)