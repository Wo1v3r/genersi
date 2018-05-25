from settings import functions, terminals, arguments, numbers
from treelib import Node, Tree
import random

class TreeBuilder:
  def __init__(self, MAX_DEPTH = 10):
    self.currentId = 0
    self.MAX_DEPTH = MAX_DEPTH

  def grow(self, tree, depth, parent = None, full = False):
    aTerminal = random.choice(list(terminals.keys() ) + numbers)
    aFunction = random.choice(list(functions.keys()))
    isATerminal = full and random.choice([True, False])

    if depth == self.MAX_DEPTH or isATerminal:
      tree.create_node(aTerminal, self.currentId, parent=parent)

    else:
      tree.create_node(aFunction, self.currentId, parent=parent)  
      me = self.currentId
      
      for _ in range(arguments(aFunction)):
        self.currentId += 1
        self.grow(tree, depth+1, parent = me , full = full)

  def halfAndHalf(self):
    self.currentId = 0;
    tree = Tree()
    full = random.choice([True, False])
    self.grow(tree,0,full=full)
    return tree
