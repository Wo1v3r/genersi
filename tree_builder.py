from settings import functions, terminals, arguments, numbers
from treelib import Node, Tree
import random

class TreeBuilder:
  def __init__(self, MAX_DEPTH = 10):
    self.MAX_DEPTH = MAX_DEPTH

  def grow(self, tree, depth, parent = None, full = False):
    aTerminal = random.choice(list(terminals.keys() ) + numbers)
    aFunction = random.choice(list(functions.keys()))
    isATerminal = full and random.choice([True, False])

    if depth == self.MAX_DEPTH or isATerminal:
      tree.create_node(aTerminal, parent=parent)

    else:
      node = tree.create_node(aFunction, parent=parent)  
      me = node.identifier
      
      for _ in range(arguments(aFunction)):
        self.grow(tree, depth+1, parent = me , full = full)

  def halfAndHalf(self):
    tree = Tree()
    full = random.choice([True, False])
    self.grow(tree,0,full=full)
    return tree
