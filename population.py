import random
from individual import IndividualFactory


class Population:
  def __init__(self, POP_SIZE = 2):
    self.POP_SIZE = POP_SIZE
    self.items = [IndividualFactory.prototype() for _ in range(POP_SIZE)]

  def select(self, omit=None):
    items = [item for item in self.items if omit is None or item.id != omit.id]
    item1 = random.choice(items)
    item2 = random.choice(items)

    return item1 if item1 > item2 else item2
  
  def reproduce(self):
    newBorn = self.select()
    newBorn = IndividualFactory.crossOver(newBorn, self.select(omit=newBorn)) if random.random() < 0.9 else newBorn
    
    newBorn = IndividualFactory.mutate(newBorn) if random.random() < 0.01 else newBorn

    return newBorn
  
  def moveGeneration(self):
    self.nextGeneration = []
    
    for _ in range(self.POP_SIZE):
      self.nextGeneration.append(self.reproduce())
    
    self.items = self.nextGeneration