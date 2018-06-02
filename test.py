import sys
from human import (
    enterPlayerTile,
    whoGoesFirst,
    drawBoard, 
    showPoints,
    getScoreOfBoard,
    getPlayerMove,
    playAgain
)
from game import (
    getNewBoard,
    resetBoard,
    getBoardWithValidMoves,
    makeMove,
    getValidMoves
)
from algorithm import evaluateBoard
from constants import PLAYER_X, PLAYER_O

class Test():
    def __init__(self, item):
        self.item = item

    def play(self):
        while True:
            mainBoard = getNewBoard()
            resetBoard(mainBoard)
            playerTile, computerTile = enterPlayerTile()
            showHints = False
            turn = whoGoesFirst()
            print('The ' + turn + ' will go first.')

            while True:
                if turn == 'player':
                    # Player's turn.
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
                    else:
                        makeMove(mainBoard, playerTile, move[0], move[1])

                    if getValidMoves(mainBoard, computerTile) == []:
                        break
                    else:
                        turn = 'computer'

                else:
                    # Computer's turn.
                    drawBoard(mainBoard)
                    showPoints(playerTile, computerTile, mainBoard)
                    raw_input('Press Enter to see the computer\'s move.')
                    x, y = evaluateBoard(mainBoard, computerTile, 2,  self.item)
                    makeMove(mainBoard, computerTile, x, y)

                    if getValidMoves(mainBoard, playerTile) == []:
                        break
                    else:
                        turn = 'player'

            # Display the final score.
            drawBoard(mainBoard)
            scores = getScoreOfBoard(mainBoard)
            print('X scored %s points. O scored %s points.' % (scores[PLAYER_X], scores[PLAYER_O]))
            if scores[playerTile] > scores[computerTile]:
                print('You beat the computer by %s points! Congratulations!' % (scores[playerTile] - scores[computerTile]))
            elif scores[playerTile] < scores[computerTile]:
                print('You lost. The computer beat you by %s points.' % (scores[computerTile] - scores[playerTile]))
            else:
                print('The game was a tie!')

            if not playAgain():
                break