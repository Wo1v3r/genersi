from constants import *
from treelib import Node, Tree

getScoreOfPlayerTree = Tree()

getScoreOfPlayerTree.create_node(IF, 0)

getScoreOfPlayerTree.create_node(EQUALS, 1, parent=0)
getScoreOfPlayerTree.create_node(MINUS, 2, parent=0)
getScoreOfPlayerTree.create_node(MINUS, 3, parent=0)

getScoreOfPlayerTree.create_node(PLAYER, 4, parent=1)
getScoreOfPlayerTree.create_node(PLAYER_X, 5, parent=1)

getScoreOfPlayerTree.create_node(PLAYER_X_SCORE, 6, parent=2)
getScoreOfPlayerTree.create_node(PLAYER_O_SCORE, 7, parent=2)

getScoreOfPlayerTree.create_node(PLAYER_O_SCORE, 8, parent=3)
getScoreOfPlayerTree.create_node(PLAYER_X_SCORE, 9, parent=3)

# getScoreOfPlayerTree.show()

