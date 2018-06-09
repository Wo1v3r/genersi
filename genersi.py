import sys, traceback
from settings.constants import PLAYER_X, PLAYER_O
from settings.variables import MAX_DEPTH, IS_TOURNAMENT, GENERATIONS
from evolution.individual import IndividualFactory
from evolution.population import Population
from evolution.fitness import fitness
from utils.timer import startTimer
from utils.reporter import report

currentTime = startTimer()
population = Population()

try:
  for genaration in range(GENERATIONS):
    print(currentTime() + '\t| Generation number: ' + str(genaration))
    num = 0

    for item in population.items:
      num += 1
      fitness(item = item, items=population.items,  num=num)
      print(currentTime() + '\t| Item ' + str(num) + ' With Fitness: ' + str(item.fitness))

    population.moveGeneration()

except KeyboardInterrupt:
  traceback.print_exc(file=sys.stdout)
  pass


best_player = population.best()

print(currentTime() + '\t| Experiment Over')


report(item=best_player)

