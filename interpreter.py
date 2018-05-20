from settings import functions, terminals


def invoke(board, player ,node ,children, values):
  resolvedValues = {}
  evaluator = functions[node.tag]

  for child in children:
    resolvedValues[child.tag] = values[child.tag](board,player)

    if callable(resolvedValues[child.tag]):
      resolvedValues[child.tag] = values[child.tag](values)
  
  return evaluator(resolvedValues)


def parse_tree(id, tree):
  node = tree.get_node(id)

  if node.is_leaf() and node.tag in terminals:
    return terminals[node.tag]

  if not node.is_leaf() and node.tag in functions:
    values = {}
    values.clear()
    children = tree.children(id)

    for child in children:
      values[child.tag] = parse_tree(child.identifier, tree)

    return lambda board,player: invoke(board,player,node,children,values)

  return lambda board,player: node.tag