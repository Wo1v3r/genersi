from constants import *
from treelib import Node, Tree

getScoreOfPlayerTree = Tree()

getScoreOfPlayerTree.create_node(IF, 0)

getScoreOfPlayerTree.create_node(CONDITION, 1, parent=0)
getScoreOfPlayerTree.create_node(EQUALS, 4, parent=1)
getScoreOfPlayerTree.create_node(PLAYER, 7, parent=4)
getScoreOfPlayerTree.create_node(PLAYER_X, 8, parent=4)

getScoreOfPlayerTree.create_node(THEN, 2, parent=0)
getScoreOfPlayerTree.create_node(MINUS, 5, parent=2)
getScoreOfPlayerTree.create_node(PLAYER_X_SCORE, 9, parent=5)
getScoreOfPlayerTree.create_node(PLAYER_O_SCORE, 10, parent=5)

getScoreOfPlayerTree.create_node(ELSE, 3, parent=0)
getScoreOfPlayerTree.create_node(MINUS, 6, parent=3)
getScoreOfPlayerTree.create_node(PLAYER_O_SCORE, 11, parent=6)
getScoreOfPlayerTree.create_node(PLAYER_X_SCORE,12, parent=6)
getScoreOfPlayerTree.show()