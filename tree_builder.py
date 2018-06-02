from settings import functions, terminals, arguments, numbers
from treelib import Node, Tree
import uuid
import random

class TreeBuilder:
  def __init__(self, MAX_DEPTH = 10):
    self.MAX_DEPTH = MAX_DEPTH

  def grow(self, tree, depth, parent = None, full = False):
    aTerminal = random.choice(list(terminals.keys() ) + numbers)
    aFunction = random.choice(list(functions.keys()))
    isATerminal = not full and random.choice([True, False])

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

def regenerate_ids(tree):
  nodes = [ tree[node] for node in tree.expand_tree(mode=Tree.DEPTH) ]
  for node in nodes:
    kids = tree.children(node.identifier)
    isRoot = tree.root == node.identifier
    if not kids and isRoot:
      newTree = Tree()
      newTree.create_node(tag=node.tag)
      tree=newTree
    elif isRoot:
      tree.get_node(tree.root).bpointer = None
      tree.update_node(node.identifier, identifier=str(uuid.uuid1()))
    else:
      tree.update_node(node.identifier, identifier=str(uuid.uuid1()))