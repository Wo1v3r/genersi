import sys
from play.champion import contestChampion

isComputer = False
difficulty = 'Master'

if len(sys.argv) > 1:
  isComputer = sys.argv[1] == '--computer'

if len(sys.argv) > 2:
  difficulty = sys.argv[2].split("--")[1]


contestChampion(isComputer = isComputer, difficulty=difficulty)
