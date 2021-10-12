# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        William Taylor
#               David Tanase
#               Henry Reinhardt
#               Timothy Bui
# Section:      209
# Assignment:   THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date:         DAY MONTH YEAR
#

bp = '@'  # Black Piece
wp = 'O'  # White Piece
sp = '.'  # Empty Space
board = [[sp, bp, sp, bp, sp, bp, sp, bp],
         [bp, sp, bp, sp, bp, sp, bp, sp],
         [sp, bp, sp, bp, sp, bp, sp, bp],
         [sp, sp, sp, sp, sp, sp, sp, sp],
         [sp, sp, sp, sp, sp, sp, sp, sp],
         [wp, sp, wp, sp, wp, sp, wp, sp],
         [sp, wp, sp, wp, sp, wp, sp, wp],
         [wp, sp, wp, sp, wp, sp, wp, sp]]
row = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def printBoard():  # Prints the current status of the board
    for i in range(8):
        print(8-i, end="  ")
        for o in range(8):
            print(board[i][o], end="  ")
        print()
    print("", end="")
    for i in range(9):
        print(row[i], end="  ")
    print()

printBoard()
value = input("Enter your move: ")

def getMove(move): # move is a list     Example: ["A3", "B4"]
    startPos = [8-int(move[0][1:]), row.index(move[0][:1])-1]
    endPos = [8-int(move[1][1:]), row.index(move[1][:1])-1]

    if(board[startPos[0]][startPos[1]] == "."):
        print("There is no piece at this position")
        print("Try again")
    elif((endPos[0] + endPos[1]) %2 == 0):
        print("This is not a valid move - Must move to a dark square")
        print("Try again")
    elif(board[endPos[0]][endPos[1]] == board[startPos[0]][startPos[1]]):
        print("This is not a valid - You can not move onto your own piece")
        print("Try again")
    else:
        board[endPos[0]][endPos[1]] = board[startPos[0]][startPos[1]]
        board[startPos[0]][startPos[1]] = '.'


while value != 'stop':  # Game loop
    print("\n\n")
    move = value.split(" ")
    getMove(move)
    printBoard()
    value = input("Enter your move: ")
