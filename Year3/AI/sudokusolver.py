__author__ = "Tay Hui Lian"
__doc__ = '''This is sudoku solver I made from my free time after AI exam.
This uses constraint propagation where each move will propagate the
constraints(by removing the number) to other square's searchspace.'''

board = [[] for i in range(9)]

# initialization - note that changes to this board will need to change the asserts statements below.
board[0] = [0,0,9,3,0,6,0,0,8]
board[1] = [8,1,0,5,2,0,0,7,0]
board[2] = [0,5,0,0,8,0,0,2,0]
board[3] = [9,0,3,0,0,0,0,0,0]
board[4] = [0,7,2,9,6,4,3,8,0]
board[5] = [0,0,0,0,0,0,2,0,9]
board[6] = [0,9,0,0,3,0,0,4,0]
board[7] = [0,3,0,0,4,5,0,9,2]
board[8] = [5,0,0,8,0,7,6,0,0]

# initialize searchspace
searchspace = [[[k for k in range(1,10)]for j in range(9)] for i in range(9)]
def removesearchspace(board, searchspace):
    for i in range(9):
        for j in range(9):
            if board[i][j]>0:
                searchspace[i][j] = []

def outputboard(board):
    print "==== board ===="
    for i in range(9):
        for j in range(9):
            print "%d" %board[i][j],
        print
    print "==============="
def violatehorizontal(board, r, c, value):
    if value in board[r]:
        return True
    return False
def violatevertical(board, r, c, value):
    if value in [board[i][c] for i in range(9)]:
        return True
    return False
def violate3x3(board, r, c, value):
    index_r = (r/3)*3
    index_c = (c/3)*3
    tmp = []
    for i in range(index_r, index_r + 3):
        for j in range(index_c, index_c + 3):
            tmp.append(board[i][j])
    if value in tmp:
        return True
    return False
def removefromsearchspace(lst, toremove):
    for i in toremove:
        lst.remove(i)
def outputsearchspace(searchspace):
    print "=== searchspace ==="
    for i in range(9):
        for j in range(9):
            print "(%d, %d):" % (i, j), searchspace[i][j]
    print "=== searchspace ==="
def propagateconstraint(searchspace, r, c, value):
    for i in range(9):
        try:
            searchspace[i][c].remove(value)         # remove from verticals
        except ValueError:
                pass
        try:
            searchspace[r][i].remove(value)         # remove from horizontals
        except ValueError:
                pass
    index_r = (r/3)*3
    index_c = (c/3)*3
    for i in range(index_r, index_r + 3):
        for j in range(index_c, index_c + 3):
            try:
                searchspace[i][j].remove(value)     # remove from 3x3 grid.
            except ValueError:
                pass

#outputboard(board)
removesearchspace(board, searchspace)

# unit testing of functions
assert violatehorizontal(board, 0, 7, 9) == True
assert violatehorizontal(board, 1, 5, 9) == False
assert violatevertical(board, 5, 2, 9) == True
assert violatevertical(board, 1, 5, 9) == False
assert violate3x3(board, 1, 2, 5) == True
assert violate3x3(board, 1, 2, 6) == False

# first level search (will reduce the search space a lot).
for i in range(9):
    for j in range(9):
        if searchspace[i][j]:
            toremove = []                                           # cannot remove while enumerating. probably due to race condition.
            for possible in searchspace[i][j]:
                if violatehorizontal(board, i, j, possible) or violatevertical(board, i, j, possible) or violate3x3(board, i, j, possible):
                    toremove.append(possible)
            removefromsearchspace(searchspace[i][j], toremove)      # eliminate violated - remove in 1 shot
            toremove = []

assert searchspace[0][0] == [2,4,7]
assert searchspace[0][4] == [1,7]

outputboard(board)

def writeanswer():
    for i in range(9):
        for j in range(9):
            if len(searchspace[i][j]) == 1:                 # the only possible answer
                value = searchspace[i][j][0]
                print "confirmed:", (i, j), "=", value
                board[i][j] = value
                propagateconstraint(searchspace, i, j, value)
                return None

#outputsearchspace(searchspace)

writeanswer()

outputboard(board)

assert board[1][5] == 9

#outputsearchspace(searchspace)

count = 1

def endgame(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True

while(not endgame(board)):
    writeanswer()
    outputboard(board)
    count+=1
print "end game"
print count
