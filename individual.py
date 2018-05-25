from interpreter import parse_tree
from tree_builder import TreeBuilder

class Individual:
  def __init__(self, tree):
    self.tree = tree
    self.eval = parse_tree(0 , self.tree)


class IndividualFactory:
  @staticmethod
  
  def prototype():
    builder = TreeBuilder(MAX_DEPTH=3);
    tree = builder.halfAndHalf()
    tree.show()
    return Individual(tree)

  @staticmethod
  def fromTree(tree):
    return Individual(tree)

  
  # @staticmethod
  # def crossOver(individualA, individualB):
  #   subtreeA = individualA.tree.pickSubtree()
  #   subtreeB = individualB.tree.pickSubtree()

  #   return Individual(subtreeA.join(subtreeB));