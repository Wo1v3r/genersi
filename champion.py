
import sys , json

from play.test import Test
from utils.tree_builder import TreeBuilder
from evolution.individual import IndividualFactory

with open('champion.tree.json', 'r') as readFile:
    best_player_json = json.load(readFile)

best_player_tree = TreeBuilder.fromJson(best_player_json)
best_player = IndividualFactory.fromTree(best_player_tree)

game_v_human = Test(best_player)


isComputer = False

if len(sys.argv) > 1:
  isComputer = sys.argv[1] == '--computer'

game_v_human.play(isComputer= isComputer)