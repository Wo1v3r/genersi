from settings.nodes import functions, terminals

def invoke(board, player ,tag, values):
  evaluator = functions[tag]
  resolvedValues = [ _(board,player) for _ in values]
  return evaluator(resolvedValues)


def parse_tree(id, tree):
  node = tree.get_node(id)

  if node.tag in functions:
    children = tree.children(id)
    values = [parse_tree(child.identifier,tree) for child in children]

    def invoker(board,player):
      tag = node.tag
      return invoke(board=board,player=player,tag=tag,values=values)
    
    return invoker

  def toInt(board,player):
    tag = node.tag
    
    value = 0

    try:
      value = int(tag)
    
    except Exception:
      value = terminals[tag](board,player)

    return value
  
  return toInt


def evaluate_tree(tree):
  return parse_tree(tree.root, tree)
