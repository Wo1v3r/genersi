
import json
from play.test import Test
from utils.tree_builder import TreeBuilder
from evolution.individual import IndividualFactory

def loadChampion():
  with open('champion.tree.json', 'r') as readFile:
      champion_json = json.load(readFile)

  champion_tree = TreeBuilder.fromJson(champion_json)
  champion_item = IndividualFactory.fromTree(champion_tree)

  return champion_item

def contestChampion(isComputer = False, item = loadChampion()):
  game_v_human = Test(item)
  return game_v_human.play(isComputer = isComputer)

