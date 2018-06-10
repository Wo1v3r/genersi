import sys, traceback
from settings.constants import PLAYER_X, PLAYER_O
from settings.variables import MAX_DEPTH, IS_TOURNAMENT, GENERATIONS
from evolution.individual import IndividualFactory
from evolution.population import Population
from evolution.fitness import fitness
from utils.timer import startTimer
from utils.reporter import openReport, closeReport
from play.champion import contestChampion

currentTime = startTimer()
population = Population()
experimentDir = openReport()
currentGeneration = 0
generationFitness = {}

try:
  for generation in range(GENERATIONS):
    all_fitness = []

    currentGeneration = generation
    print(currentTime() + '\t| Generation number: ' + str(generation))
    num = 0

    for item in population.items:
      num += 1
      
      if GENERATIONS == generation + 1:
        fitness(item = item, items=population.items,  num=num, isTournament=True)
      else:
        fitness(item = item, items=population.items,  num=num)
        
      print(currentTime() + '\t| Item ' + str(num) + ' With Fitness: ' + str(item.fitness))
      all_fitness.append(item.fitness)

    generationFitness[str(generation + 1)] = all_fitness
    population.moveGeneration()

except Exception:
  traceback.print_exc(file=sys.stdout)
  pass


best_player = population.best()
experimentTime = currentTime()
print('%s\t| Experiment Over' % experimentTime)

print('Contesting champion:')

results = {
  'Noob': contestChampion(isComputer=True, item = item, difficulty= 'NOOB'),
  'Adept': contestChampion(isComputer=True, item = item, difficulty= 'NOOB'),
  'Master': contestChampion(isComputer=True, item = item, difficulty= 'NOOB')
}

closeReport(
  item=best_player,
  experimentTime=experimentTime,
  generation = currentGeneration,
  results = results,
  generationFitness = generationFitness,
  experimentDir = experimentDir
)