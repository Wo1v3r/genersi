import sys
import random
from human import (
    enterPlayerTile,
    rollPlayerTile,
    whoGoesFirst,
    drawBoard, 
    showPoints,
    getScoreOfBoard,
    getPlayerMove
)
from game import (
    getNewBoard,
    resetBoard,
    getBoardWithValidMoves,
    makeMove,
    getValidMoves,
    getComputerMove
)
from algorithm import evaluateBoard
from constants import PLAYER_X, PLAYER_O, GAME_COUNT

class Test():
    def __init__(self, item):
        self.item = item

    def play(self, isComputer = False):

        game_count = GAME_COUNT if isComputer else 1
        game_wins = 0

        for _ in range(game_count):
          mainBoard = getNewBoard()
          resetBoard(mainBoard)
          

          turn = whoGoesFirst()
          showHints = False
          
          if not isComputer:
            playerTile, computerTile = enterPlayerTile()
            print(turn + ' will go first.')

          else:
            playerTile, computerTile = rollPlayerTile()

          while True:
              if turn == 'player':
                  
                  if isComputer:
                    move = getComputerMove(mainBoard, playerTile)  
                  
                  else : 
                    if showHints:
                        validMovesBoard = getBoardWithValidMoves(mainBoard, playerTile)
                        drawBoard(validMovesBoard)
                    else:
                        drawBoard(mainBoard)
                    showPoints(playerTile, computerTile, mainBoard)
                    move = getPlayerMove(mainBoard, playerTile)
                  
                    if move == 'quit':
                        print('Thanks for playing!')
                        sys.exit() # terminate the program
                  
                    elif move == 'hints':
                        showHints = not showHints
                        continue
                  
                  makeMove(mainBoard, playerTile, move[0], move[1])

                  if getValidMoves(mainBoard, computerTile) == []:
                      break
                  
                  else:
                      turn = 'computer'

              else:
                  if not isComputer:
                    drawBoard(mainBoard)
                    showPoints(playerTile, computerTile, mainBoard)
                    
                    # raw_input('Press Enter to see the computer\'s move.') #python 2
                    input('Press Enter to see the computer\'s move.') #python 3

                  x, y = evaluateBoard(mainBoard, computerTile, 2,  self.item)
                  makeMove(mainBoard, computerTile, x, y)

                  if getValidMoves(mainBoard, playerTile) == []:
                      break
                  else:
                      turn = 'player'

          if not isComputer:
            drawBoard(mainBoard)
          
          scores = getScoreOfBoard(mainBoard)
          
          if not isComputer:
            print('X scored %s points. O scored %s points.' % (scores[PLAYER_X], scores[PLAYER_O]))
          
          if scores[playerTile] > scores[computerTile]:
            if isComputer:
              print('Computer beat the champion by %s points! Boo!' % (scores[playerTile] - scores[computerTile]))
            else:
              print('You beat the Champion by %s points! Boo!' % (scores[playerTile] - scores[computerTile]))
          
          elif scores[playerTile] < scores[computerTile]:
            game_wins += 1

            if isComputer:
              print('Champion beat the computer by %s points! Congratulations!' % (scores[computerTile] - scores[playerTile]))
            else:
              print('Champion beat yo ass by %s points! Congratulations!' % (scores[computerTile] - scores[playerTile]))
          
          else:
              print('The game was a tie!')
          
          print('')
          
        if isComputer:
          print('Champion won %d out of %d games' % (game_wins, game_count))