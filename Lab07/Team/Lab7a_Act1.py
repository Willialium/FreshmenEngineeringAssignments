# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        William Taylor
#               David Tanase
#               Henry Reinhardt
#               Timothy Bui
# Section:      209
# Assignment:   7-2
# Date:         15 10 2021
#

#  Board array
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

# Column labels array
row = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# Prints the current status of the board

def printBoard():
    for i in range(8):
        print(8-i, end="  ")
        for o in range(8):
            print(board[i][o], end="  ")
        print()
    print("", end="")
    for i in range(9):
        print(row[i], end="  ")
    print()

#  Checks the validity of each move input
def getMove(move): # move is a list     Example: ["A3", "B4"]
    startPos = [8-int(move[0][1:]), row.index(move[0][:1])-1]
    endPos = [8-int(move[1][1:]), row.index(move[1][:1])-1]

    if(board[startPos[0]][startPos[1]] == "."):
        print("There is no piece at this position")
        print("Try again")
    elif((endPos[0] + endPos[1]) %2 == 0):
        print("This is not a valid move - Must move to a dark square")
        print("Try again")
    else:
        board[endPos[0]][endPos[1]] = board[startPos[0]][startPos[1]]
        board[startPos[0]][startPos[1]] = '.'

#  Prints instructions to the user

print("\n\n***** INSTRUCTIONS *****")
print("A coordinate is entered as column(letter) row(number) such as A1 or H7")
print("When entering a move, enter the starting coordinate of the piece followed by a space and the ending coordinate of the piece")
print("Example: A1 A3")
print("************************\n\n")

#  Starts the game with getting input and calling methods

printBoard()
value = input("Enter your move: ")

while value != 'stop':  # Game loop
    print("\n\n")
    move = value.split(" ")
    getMove(move)
    printBoard()
    value = input("Enter your move: ")

print("Thanks for playing")