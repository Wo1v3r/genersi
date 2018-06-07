import random
import time
from test import Test
from algorithm import evaluateBoard


from game import (
    getNewBoard,
    resetBoard,
    getComputerMove,
    makeMove,
    getScoreOfPlayer,
    winner,
    gameOver
)
from constants import PLAYER_X, PLAYER_O, GENERATIONS, POPULATION_SIZE
from individual import IndividualFactory
from population import Population
from concurrent.futures import ThreadPoolExecutor
from threading import RLock
from tree_builder import TreeBuilder

print_rlock = RLock()

def startTimer():
  startExperiment = time.time()
  
  def currentTime():

    return str(time.time() - startExperiment)
  
  return currentTime

currentTime = startTimer()

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

    step = evaluateBoard(board, PLAYER_O, 2,  player2)

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

def fitness(item, num):
    otherItem = random.choice(population.items)
    game = Game(item, otherItem)
    game.play()
    item.fitness = game.playerScore
    
    # with print_rlock:
    print(currentTime() + '\t| Item ' + str(num) + ' Scored: ' + str(game.playerScore))


population = Population(POPULATION_SIZE)

for genaration in range(GENERATIONS):
  print(currentTime() + '\t| Generation number: ' + str(genaration))
  
  num = 0
  
  # with ThreadPoolExecutor() as executor:
  for item in population.items:
    num += 1
    # executor.submit(fitness, item=item, num=num)
    fitness(item,num)
  
  population.moveGeneration()

# Getting the best player item
best_player = population.items[0]
for item in population.items:
  if item > best_player:
    best_player = item


print(currentTime() + '\t| Experiment Over')

print("Best player genotype:")
best_player.tree.show()
best_player.tree.save2file('champion.tree')
print("Saved to ./champion.tree")


# Play versus human
game_v_human = Test(best_player)
game_v_human.play()