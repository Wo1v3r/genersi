from game import getScoreOfBoard

functions = {
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
  'getScoreOfPlayerO': lambda board, player:  getScoreOfBoard(board)['O'],
  'getScoreOfPlayerX': lambda board, player : getScoreOfBoard(board)['X']
}
