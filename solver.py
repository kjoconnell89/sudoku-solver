'''
A program to solve any given sudoku board, assuming it is solvable, utilizing backtracking algorithm
'''


#0s represent empty spaces -- would have used # but that would require string / int conversions
startingBoard = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

#these are permanent values across any iteration of a board
subGrids = [
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)], #subgrid 1
    [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)], #subgrid 2
    [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)], #subgrid 3
    [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 1), (5, 0), (5, 1), (5, 2)], #subgrid 4
    [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)], #subgrid 5
    [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)], #subgrid 6
    [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 1), (8, 0), (8, 1), (8, 2)], #subgrid 7
    [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)], #subgrid 8
    [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)] #subgrid 9
]

#replicating here just to have reference points
currentBoard = startingBoard.copy()

def prettyBoard(currentBoard): 
    #prints board in the following manner to match sudoku format
    '''
    -------------
    |###|###|###|
    |###|###|###|
    |###|###|###|
    -------------
    |###|###|###|
    |###|###|###|
    |###|###|###|
    -------------
    |###|###|###|
    |###|###|###|
    |###|###|###|
    -------------
    '''

    '''should always be a 9 x 9 board, don't need to make range dynamic
    i = row number, j = column number'''
    if  len(currentBoard) != 9:
        print('Not enough rows in the board - expected 9, input {}'.format(len(startingBoard)))
        return False
    
    else:
        for i in range(9):
            if len(currentBoard[i]) != 9:
                print('Not enough columns in the board for row {} - expected 9, input {}'.format(i, len(currentBoard[i])))
                return False
            
            else:
                if (i % 3 == 0):
                    print('-------------')

                for j in range(9):
                    if (j % 3 == 0):
                        print('|', end = '')
                    
                    print(currentBoard[i][j], end = '')

                    if (j == 8):
                        print('|\n', end = '')

                if (i == 8):
                    print('-------------')


def findUnpopulated(currentBoard):
    '''should always be a 9 x 9 board, don't need to make range dynamic
    i = row number, j = column number'''
    for i in range(9):
        for j in range(9):
            if currentBoard[i][j] == 0:
                return (i, j)

    return False                


def validatePosition(currentBoard, position, value, subGrids):
    '''should always be a 9 x 9 board, don't need to make range dynamic
    i = row number, j = column number
    rules:
    -no duplicate value in row
    -no duplicate value in column
    -no duplicate value in 3x3 subgrid (visualized below) (values will decremented by 1 in array utilization - subgrid definition above)
    -------
    |1|2|3|
    -------
    |4|5|6|
    -------
    |7|8|9|
    -------
    '''

    x = position[0]
    y = position[1]

    #validate row
    #check each element (column) in row and see if equal to number that we are adding in (value). dont check for position that we just added value to
    for i in range(9):
        if currentBoard[x][i] == value and y != i: 
            print('{} does not work in ({}, {}) due to row'.format(value, x, y))
            return False
    
    #validate column
    #check each element (row) in column and see if equal to number that we are adding in (value). dont check for position that we just added value to
    for j in range(9):
        if currentBoard[j][y] == value and x != j: 
            print('{} does not work in ({}, {}) due to column'.format(value, x, y))
            return False


    #validate subgrid
    #determine the subgrid in which the input position resides, then translate that subgrid to the current board state to determine if number we are adding already exists
    #can maybe use integer division on position parameter to determine subgrid -> posX // 3 & posY // 3  
    for section in subGrids:
        if position in section:
            if value in currentBoard[subGrids.index(section)]:
                print('{} does not work in ({}, {}) due to subgrid'.format(value, x, y))
                return False


    #all rules satisfied
    return True


def solveBoard(currentBoard):
    something = findUnpopulated(currentBoard)
    
    #returning position of empty space, if board is full returns false
    if not something:
        return True
    else:
        (x, y) = something
        #print(something)

    #want to explicitly try values 1-9 as those are what should be populated according to the rules
    for i in range(1, 10):
        #determine if number is valid in specified position, and if so change the state of the board to reflect that
        if validatePosition(currentBoard, (x, y), i, subGrids):
            print('{} put in {}'.format(i, (x,y)))
            currentBoard[x][y] = i

            #recursively attempt to fill in the remaining empty spaces
            if solveBoard(currentBoard):
                return True

            #if we loop through 1-9 and no value is correct, the recursive call above should hit false and therefore 
            #that position needs to be backed out
            print('backing out ({}, {})'.format(x, y))
            currentBoard[x][y] = 0

    return False


print(prettyBoard(currentBoard))
print('*************')
solveBoard(currentBoard)
#print()
#print('*************')
#print()
#print(prettyBoard(currentBoard))
#print(validatePosition(currentBoard, (0,2), 5, subGrids))
#print(findUnpopulated(currentBoard))

###subgrid logic needs to be reviewed
###trying to put 9 in (0,4) gives false subgrid error