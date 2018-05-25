from settings import functions, terminals


def invoke(board, player ,node ,values):
  evaluator = functions[node.tag]
  resolvedValues = [ _(board,player) for _ in values]
  return evaluator(resolvedValues)


def memoize(f):
  cache = {}

  def memoized(board,player):
    hashed = str((board,player))

    if hashed not in cache:
      cache[hashed] = f(board,player)

    return cache[hashed]

  return memoized


def parse_tree(id, tree):
  node = tree.get_node(id)

  if node.is_leaf() and node.tag in terminals:
    return terminals[node.tag]

  if not node.is_leaf() and node.tag in functions:
    children = tree.children(id)
    values = [parse_tree(child.identifier,tree) for child in children]

    return lambda board,player: invoke(board,player,node,values)

  return lambda board,player: int(node.tag)


def evaluate_tree(tree):
  return memoize(parse_tree(tree.root, tree))
