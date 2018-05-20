from treelib import Node, Tree
from algorithm import *
from game import *

def getScoreOfBoard(board):
    # Determine the score by counting the tiles. Returns a dictionary with keys 'X' and 'O'.
    xscore = 0
    oscore = 0

    for x in range(8):
        for y in range(8):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1

    return {'X':xscore, 'O':oscore}


def getScoreOfPlayerX(board):
  return getScoreOfBoard(board)['X']


def getScoreOfPlayerO(board):
  return getScoreOfBoard(board)['O']

operations = {
  'if':  lambda values : values['then'] if values['condition'] else values['else'],
  'equals':  lambda values : list(values.values())[0] == list(values.values())[1],
  'minus': lambda values : list(values.values())[0] - list(values.values())[1],
  'condition': lambda values:  list(values.values())[0],
  'then': lambda values : list(values.values())[0],
  'else':  lambda values : list(values.values())[0],
}

terminals = {
  'X': lambda board, player: 'X',
  'O': lambda board, player: 'O',
  'player':lambda board, player: player,
  'getScoreOfPlayerO': lambda board, player:  getScoreOfPlayerO(board),
  'getScoreOfPlayerX': lambda board, player : getScoreOfPlayerX(board)
}

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


def invoke_operations(board, player ,node ,children, values):
  resolvedValues = {}
  evaluator = operations[node.tag]

  for child in children:
    resolvedValues[child.tag] = values[child.tag](board,player)

    if callable(resolvedValues[child.tag]):
      resolvedValues[child.tag] = values[child.tag](values)
  
  return evaluator(resolvedValues)


def parse_tree(id, tree):
  node = tree.get_node(id)

  if node.is_leaf() and node.tag in terminals:
    return terminals[node.tag]

  if not node.is_leaf() and node.tag in operations:
    values = {}
    values.clear()
    children = tree.children(id)

    for child in children:
      values[child.tag] = parse_tree(child.identifier, tree)

    return lambda board,player: invoke_operations(board,player,node,children,values)

  return lambda board,player: node.tag