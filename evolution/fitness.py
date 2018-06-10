import random
from settings.variables import IS_TOURNAMENT
from game.game import Game

def fitness(item, items, num, isTournament = IS_TOURNAMENT):
    otherItems = [otherItem for otherItem in items if otherItem.id != item.id] if isTournament else [random.choice(items)]
    
    item.fitness = 0
    for otherItem in otherItems:
      game = Game(item, otherItem)
      game.play()
      
      item.fitness += game.playerScore

    return item.fitness