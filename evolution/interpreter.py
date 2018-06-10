from settings.nodes import functions, terminals

def invoke(board, player ,tag, values):
  evaluator = functions[node.tag]
  resolvedValues = [ _(board,player) for _ in values]
  return evaluator(resolvedValues)


def parse_tree(id, tree):
  node = tree.get_node(id)

  if node.tag in terminals:
    return terminals[node.tag]

  if node.tag in functions:
    children = tree.children(id)
    values = [parse_tree(child.identifier,tree) for child in children]

    def invoker(board,player):
      tag = node.tag
      return invoke(board=board,player=player,tag=tag,values=values)
    
    return invoker

  def toInt(board,player):
    tag = node.tag
    return int(tag)
  
  return toInt


def evaluate_tree(tree):
  return parse_tree(tree.root, tree)
