import random
from evolution.individual import IndividualFactory
from settings.variables import CROSSOVER_RATE, MUTATION_RATE, POPULATION_SIZE, ELITISM, ELITISM_RATE

class Population:
  def __init__(self):
    self.items = [IndividualFactory.prototype() for _ in range(POPULATION_SIZE)]

  def select(self, omit=None):
    items = [item for item in self.items if omit is None or item.id != omit.id]
    item1 = random.choice(items)
    item2 = random.choice(items)

    return item1 if item1 > item2 else item2

  def best(self):
    return max(self.items)

  def reproduce(self):
    newBorn = self.select()

    newBorn = IndividualFactory.crossOver(individualA = newBorn, individualB = self.select(omit=newBorn)) if random.random() < CROSSOVER_RATE else newBorn

    newBorn = IndividualFactory.mutate(individual = newBorn) if random.random() < MUTATION_RATE else newBorn

    return newBorn
  
  def moveGeneration(self):
    self.nextGeneration = []

    if ELITISM:
      self.items.sort()
      elitesCount = int( x = round(ELITISM_RATE * POPULATION_SIZE) )

      for _ in range(elitesCount):
        elite = self.items.pop()
        self.nextGeneration.append(IndividualFactory.elitism(individual = elite))

    for _ in self.items:
      self.nextGeneration.append(self.reproduce())
    
    self.items = self.nextGeneration
