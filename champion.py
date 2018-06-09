
import json
from test import Test
from tree_builder import TreeBuilder
from individual import IndividualFactory

with open('champion.tree.json', 'r') as readFile:
    best_player_json = json.load(readFile)

best_player_tree = TreeBuilder.fromJson(best_player_json)
best_player = IndividualFactory.fromTree(best_player_tree)

game_v_human = Test(best_player)
game_v_human.play()