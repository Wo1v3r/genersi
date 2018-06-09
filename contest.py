import sys
from play.champion import contestChampion

isComputer = False

if len(sys.argv) > 1:
  isComputer = sys.argv[1] == '--computer'

contestChampion(isComputer = isComputer)
