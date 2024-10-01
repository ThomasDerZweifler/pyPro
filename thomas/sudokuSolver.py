board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

def sudoku(size):
    import time
    start_time=time.time()

    import sys
    import random as rn
    mydict = {}
    n = 0
    print("--started calculating--")
    while len(mydict) < 9:
        n += 1
        x = range(1, size+1)
        testlist = rn.sample(x, len(x))

        isgood = True
        for dictid,savedlist in mydict.items():
            if isgood == False:
                break
            for v in savedlist:
                if testlist[savedlist.index(v)] == v:
                    isgood = False
                    break

        if isgood == True:
            isgoodafterduplicatecheck = True
            mod = len(mydict) % 3
            dsavedlists = {}
            dtestlists = {}
            dcombindedlists = {}
            for a in range(1,mod + 1):
                savedlist = mydict[len(mydict) - a]               
                for v1 in savedlist:
                    modsavedlists = (savedlist.index(v1) / 3) % 3
                    dsavedlists[len(dsavedlists)] = [modsavedlists,v1]
                for t1 in testlist:
                    modtestlists = (testlist.index(t1) / 3) % 3
                    dtestlists[len(dtestlists)] = [modtestlists,t1]
                for k,v2 in dsavedlists.items():
                    dcombindedlists[len(dcombindedlists)] = v2
                    dcombindedlists[len(dcombindedlists)] = dtestlists[k]
            vsave = 0
            lst1 = []
            for k, vx in dcombindedlists.items():
                vnew = vx[0]
                if not vnew == vsave:
                    lst1 = []
                    lst1.append(vx[1])
                else:
                    if vx[1] in lst1:
                        isgoodafterduplicatecheck = False
                        break
                    else:
                        lst1.append(vx[1])
                vsave = vnew

            if isgoodafterduplicatecheck == True:

                mydict[len(mydict)] = testlist
                print ('success found'), len(mydict), 'row'   

    print( '--finished calculating--\n')
    total_time = time.time()-start_time
    return mydict, n, total_time

def sudokuGenerator2():
    from random import sample

    base  = 3
    side  = base*base

    # pattern for a baseline valid solution
    def pattern(r,c): return (base*(r%base)+r//base+c)%side

    # randomize rows, columns and numbers (of valid base pattern)
    from random import sample
    def shuffle(s): return sample(s,len(s)) 
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern
    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

    for line in board: print(line)

    squares = side*side
    empties = squares * 3//4
    for p in sample(range(squares),empties):
        board[p//side][p%side] = 0

    print("\n")
    for line in board: print(line)

    solve(board)
    print("\n")
    for line in board: print(line)

sudokuGenerator2()

def sudokuGegerator():
    return_dict, total_tries, amt_of_time = sudoku(9)
    print ('generated sudoku',total_tries,'tries in', round(amt_of_time,2), 'secs :\n')
    for v in return_dict.items():
        print(v)

# sudokuGegerator()

def sudokuSolver():
    import time
    start_time=time.time()
    print ('\na given sudoku:\n')
    print_board(board)
    solve(board)
    total_time = time.time()-start_time
    print ('\nsolved into',round(total_time,10), 'secs :\n')

    print_board(board)

    print("\n")

sudokuSolver()