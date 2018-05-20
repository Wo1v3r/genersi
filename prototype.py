from treelib import Node, Tree

getScoreOfPlayerTree = Tree()

getScoreOfPlayerTree.create_node("if", 0)

getScoreOfPlayerTree.create_node("condition", 1, parent=0)
getScoreOfPlayerTree.create_node("equals", 4, parent=1)
getScoreOfPlayerTree.create_node("player",7, parent=4)
getScoreOfPlayerTree.create_node("X",8, parent=4)

getScoreOfPlayerTree.create_node("then", 2, parent=0)
getScoreOfPlayerTree.create_node("minus", 5, parent=2)
getScoreOfPlayerTree.create_node("getScoreOfPlayerX",9, parent=5)
getScoreOfPlayerTree.create_node("getScoreOfPlayerO",10, parent=5)

getScoreOfPlayerTree.create_node("else", 3, parent=0)
getScoreOfPlayerTree.create_node("minus", 6, parent=3)
getScoreOfPlayerTree.create_node("getScoreOfPlayerO",11, parent=6)
getScoreOfPlayerTree.create_node("getScoreOfPlayerX",12, parent=6)
getScoreOfPlayerTree.show()