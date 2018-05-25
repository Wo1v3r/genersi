from game import *

def drawBoard(board):
    HLINE = '  +---+---+---+---+---+---+---+---+'
    
    VLINE = '  |   |   |   |   |   |   |   |   |'

    print('    1   2   3   4   5   6   7   8')
    print(HLINE)
    for y in range(8):
        print(VLINE)
        print (y+1),
        for x in range(8):
            print ('| %s' % (board[x][y])),
        print('|')
        print(VLINE)
        print(HLINE)

def enterPlayerTile():
    # Lets the player type which tile they want to be.
    tile = ''
    while not (tile == PLAYER_X or tile == PLAYER_O):
        print('Do you want to be X or O?')
        tile = raw_input().upper()

    # the first element in the tuple is the player's tile, the second is the computer's tile.
    if tile == PLAYER_X:
        return [PLAYER_X, PLAYER_O]
    else:
        return [PLAYER_O, PLAYER_X]

def showPoints(playerTile, computerTile):
    # Prints out the current score.
    scores = getScoreOfBoard(mainBoard)
    print('You have %s points. The computer has %s points.' % (scores[playerTile], scores[computerTile]))



def getPlayerMove(board, playerTile):
    # Let the player type in their move.
    # Returns the move as [x, y] (or returns the strings 'hints' or 'quit')
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Enter your move, or type quit to end the game, or hints to turn off/on hints.')
        move = raw_input().lower()
        if move == 'quit':
            return 'quit'
        if move == 'hints':
            return 'hints'

        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break
        else:
            print('That is not a valid move. Type the x digit (1-8), then the y digit (1-8).')
            print('For example, 81 will be the top-right corner.')

    return [x, y]



def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return raw_input().lower().startswith('y')


# while True:
#     # Reset the board and game.
#     mainBoard = getNewBoard()
#     resetBoard(mainBoard)
#     playerTile, computerTile = enterPlayerTile()
#     showHints = False
#     turn = whoGoesFirst()
#     print('The ' + turn + ' will go first.')

#     while True:
#         if turn == 'player':
#             # Player's turn.
#             if showHints:
#                 validMovesBoard = getBoardWithValidMoves(mainBoard, playerTile)
#                 drawBoard(validMovesBoard)
#             else:
#                 drawBoard(mainBoard)
#             showPoints(playerTile, computerTile)
#             move = getPlayerMove(mainBoard, playerTile)
#             if move == 'quit':
#                 print('Thanks for playing!')
#                 sys.exit() # terminate the program
#             elif move == 'hints':
#                 showHints = not showHints
#                 continue
#             else:
#                 makeMove(mainBoard, playerTile, move[0], move[1])

#             if getValidMoves(mainBoard, computerTile) == []:
#                 break
#             else:
#                 turn = 'computer'

#         else:
#             # Computer's turn.
#             drawBoard(mainBoard)
#             showPoints(playerTile, computerTile)
#             raw_input('Press Enter to see the computer\'s move.')
#             x, y = getComputerMove(mainBoard, computerTile)
#             makeMove(mainBoard, computerTile, x, y)

#             if getValidMoves(mainBoard, playerTile) == []:
#                 break
#             else:
#                 turn = 'player'

#     # Display the final score.
#     drawBoard(mainBoard)
#     scores = getScoreOfBoard(mainBoard)
#     print('X scored %s points. O scored %s points.' % (scores[PLAYER_X], scores[PLAYER_O]))
#     if scores[playerTile] > scores[computerTile]:
#         print('You beat the computer by %s points! Congratulations!' % (scores[playerTile] - scores[computerTile]))
#     elif scores[playerTile] < scores[computerTile]:
#         print('You lost. The computer beat you by %s points.' % (scores[computerTile] - scores[playerTile]))
#     else:
#         print('The game was a tie!')

#     if not playAgain():
#         break