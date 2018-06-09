import random
from evolution.individual import IndividualFactory
from settings.variables import CROSSOVER_RATE, MUTATION_RATE, POPULATION_SIZE


class Population:
  def __init__(self):
    self.items = [IndividualFactory.prototype() for _ in range(POPULATION_SIZE)]

  def select(self, omit=None):
    items = [item for item in self.items if omit is None or item.id != omit.id]
    item1 = random.choice(items)
    item2 = random.choice(items)

    return item1 if item1 > item2 else item2

  def best(self):
    best_player = self.items[0]

    for item in self.items:
      if item > best_player:
        best_player = item

    return best_player
  
  def reproduce(self):
    newBorn = self.select()
    
    newBorn = IndividualFactory.crossOver(newBorn, self.select(omit=newBorn)) if random.random() < CROSSOVER_RATE else newBorn
    
    newBorn = IndividualFactory.mutate(newBorn) if random.random() < MUTATION_RATE else newBorn

    return newBorn
  
  def moveGeneration(self):
    self.nextGeneration = []
    
    for _ in range(POPULATION_SIZE):
      self.nextGeneration.append(self.reproduce())
    
    self.items = self.nextGeneration
