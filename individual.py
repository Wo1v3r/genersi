from interpreter import evaluate_tree
from tree_builder import TreeBuilder
from settings import terminals, numbers
from treelib import Tree
import uuid
import random

class Individual:
  
  def __init__(self, tree):
    self.fitness = 0
    self.id = str(uuid.uuid4())
    self.tree = tree
    self.eval = evaluate_tree(tree)


  def __gt__(self,other):
    return self.fitness > other.fitness


MAX_DEPTH=5


class IndividualFactory:
  @staticmethod
  
  def prototype():
    builder = TreeBuilder(MAX_DEPTH = MAX_DEPTH);
    tree = builder.halfAndHalf()
    tree.show()

    return Individual(tree)

  @staticmethod
  def fromTree(tree):
    return Individual(tree)

  
  @staticmethod
  def crossOver(individualA, individualB):
    tree = None

    while tree is None or tree.depth(tree.get_node(tree.root)) > MAX_DEPTH:
      treeA = Tree(tree = individualA.tree)
      treeB = Tree(tree = individualB.tree)
      removedNode = random.choice(treeA.all_nodes())
      addedNode = random.choice(treeB.all_nodes())
      
      addedSubtree = Tree(tree = treeB.subtree(addedNode.identifier))

      if removedNode.is_root():
        tree = addedSubtree

      else:
        parent = treeA.parent(removedNode.identifier)
        treeA.remove_subtree(removedNode.identifier)
        treeA.paste(parent.identifier, addedSubtree)
        tree = treeA

    return Individual(tree);


  @staticmethod
  def mutate(individual):
    aTerminal = random.choice(list(terminals.keys() ) + numbers)
    tree = Tree(tree = individual.tree)
    leaf = random.choice(tree.leaves(tree.root))

    if leaf.is_root():
      tree = Tree()
      tree.create_node(aTerminal)
    
    else:
      parent = tree.parent(leaf.identifier)
      tree.remove_subtree(leaf.identifier)      
      tree.create_node(aTerminal, parent = parent.identifier)
          
    return Individual(tree);