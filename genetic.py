import random
from algorithm import evaluateBoard
from game import getNewBoard, resetBoard, getComputerMove, makeMove, getScoreOfPlayer, winner, gameOver
from human import drawBoard
from constants import *
from individual import IndividualFactory
from population import Population

from tree_builder import TreeBuilder


class Game:
 
 def __init__(self , player, opponent):
  self.playerScore = 0
  
  self.player = player
  self.opponent = opponent

 def match(self, player1, player2):
  board = getNewBoard()
  resetBoard(board)
  
  while not gameOver(board):
    step = evaluateBoard(board, PLAYER_X, 2,  player1)
    if step is not None: 
      makeMove(board, PLAYER_X, step[0], step[1])
      # print(PLAYER_X + ' Made move: ' + str(step[0]) + ' ' + str(step[1]))
    # else:
      # print(PLAYER_X + ' Has no steps')

    step = evaluateBoard(board, PLAYER_O, 2,  player2)
    if step is not None: 
      makeMove(board, PLAYER_O, step[0], step[1])
      # print(PLAYER_O + ' Made move: ' + str(step[0]) + ' ' + str(step[1]))
    # else:
      # print(PLAYER_O + ' Has no steps')

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

population = Population()

for _ in range(3):
  for item in population.items:
    otherItem = random.choice(population.items)
    game = Game(item, otherItem)
    game.play()
    print('Item ' + item.id + ' Scored: ' + str(game.playerScore))
    item.fitness = game.playerScore
  
  population.moveGeneration()
  