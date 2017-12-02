__author__ = "Tay Hui Lian"
__doc__ = '''This minesweeper solver is a constraint satisfaction problem.
I used constraint propagation together with a lot of other techniques
like breadth first tranversal (for opening field) and
iteractive depth first tranversal of up to 2 levels to propagate constraints
to nearby squares,

Overall, this is much tougher than sudoku (observable).
because the mines are not observable hence need more techniques for discovery
:)'''

answer = [[] for i in range(9)]
# 1 = mine 0 = safe
answer[0] = [1, 0, 0, 0, 0, 1, 0, 0, 0]
answer[1] = [0, 0, 0, 0, 1, 0, 0, 0, 0]
answer[2] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
answer[3] = [0, 1, 0, 0, 0, 0, 0, 0, 0]
answer[4] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
answer[5] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
answer[6] = [0, 0, 1, 0, 1, 0, 0, 0, 0]
answer[7] = [1, 0, 0, 1, 1, 0, 1, 0, 0]
answer[8] = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def countnearbymines(r, c): # 3x3 grid
    count = 0
    row = r-1
    col = c-1
    if row < 0: row = 0     # negative index can ruin count.
    if col < 0: col = 0
    for i in range(row, r+2):
        for j in range(col, c+2):
            try:
                if answer[i][j]:
                    count += 1
            except IndexError:
                pass
    return count

# unit test.
assert countnearbymines(6, 3) == 4  # middle squares
assert countnearbymines(8, 5) == 2  # border squares
assert countnearbymines(8, 0) == 1  # corner squares

board = [['?' for j in range(9)] for i in range(9)]

def addneighbours(q, r, c):
    row = r-1
    col = c-1
    row2 = r+1
    col2 = c+1
    if row < 0: row = 0
    if col < 0: col = 0
    if row2 > 8: row2 = 8
    if col2 > 8: col2 = 8
    #print "row=", row, "row2=", row2
    #print "col=", col, "col2=", col2
    for i in range(row, row2+1):
        for j in range(col, col2+1):
            #print i, j
            if i==r and j==c:
                pass
            else:
                # never open before and not in queue
                if (board[i][j] == '?') and (not (i,j) in q):
                    q.append((i, j))

testq = []
addneighbours(testq, 0, 2)
assert testq == [(0, 1), (0, 3), (1, 1), (1, 2), (1,3)]

q = list()
def openfield(board, r, c):
    print "opening (%d, %d)" % (r, c)
    if answer[r][c] == 0:
        board[r][c] = 0
    else:
        print "game over"
        board[r][c] = "X"
        return;
    count = countnearbymines(r, c)
    if count:
        board[r][c] = count
        return;
    else: #open surrounding squares that are safe until got number. (breadth first search)
        addneighbours(q, r, c)
        while(q):
            row, col = q.pop(0)
            if answer[row][col]:
                pass
            else:
                count = countnearbymines(row, col)
                board[row][col] = count
                if count == 0:
                    addneighbours(q, row, col)
    # outputboard after finish
    outputboard()

def outputboard():
    print "===== board ====="
    for i in range(9):
        for j in range(9):
            print board[i][j],
        print
    print "================="

def getunopen(r, c):
    unopen = []
    row = r-1
    col = c-1
    row2 = r+1
    col2 = c+1
    if row < 0: row = 0
    if col < 0: col = 0
    if row2 > 8: row2 = 8
    if col2 > 8: col2 = 8
    for i in range(row, row2+1):
        for j in range(col, col2+1):
            try:
                if board[i][j] == "?":
                    unopen.append((i, j))
            except IndexError:
                pass
    return unopen

# first few opening would need some luck.
# open as many as possible.
outputboard()
openfield(board, 0, 2)
openfield(board, 3, 7)

# algorithm - constraint satisfaction problem (hmmmm)
# find the number 1 with only 1 ? square around it  - that square definitely got mine.

assert getunopen(5, 5) == [(6,4)]
assert getunopen(0, 1) == [(0,0), (1,0)]

def updateconstraints(board, r, c, level):  
    if level > 2:               # depth iterative search (cover more area than 3x3)
        return;
    numberofmines = board[r][c]
    unknown = []
    count = 0
    row = r-1
    col = c-1
    row2 = r+1
    col2 = c+1
    if row < 0: row = 0
    if col < 0: col = 0
    if row2 > 8: row2 = 8
    if col2 > 8: col2 = 8
    for i in range(row, row2+1):
        for j in range(col, col2+1):
            try:
                if board[i][j] == "?":
                    unknown.append((i, j))
                elif board[i][j] == "M":
                    count +=1
                else:
                    updateconstraints(board, i, j, level+1)
            except IndexError:
                pass
    #print "(%d, %d) count=%d, unknown=" % (r, c, count), unknown 
    if count == numberofmines: # all mines found. "?" are all deemed safe.
        for sr, sc in unknown:
            openfield(board, sr, sc)    # proceed to open fields that are safe.



def markmine():     # mark the mine and propagate constraints
    for i in range(9):
        for j in range(9):
            if board[i][j] != "?":
                possibleplaces = getunopen(i, j)
                if(len(possibleplaces) == 1 and board[i][j] != 0): # possible place definitely has a mine
                    row, col = possibleplaces[0]
                    board[row][col] = "M" # mark the place.
                    print "found mine! around (%d, %d) at (%d, %d)" % (i, j, row, col)
                    # need to propagate the constraints. (checking only nearby squares up to depth 2)
                    updateconstraints(board, i, j, 0)
                    # output
                    outputboard()
                    return;

for i in range(10):
    markmine()

print "Found all 10 mines!"
                



