'''
A program to solve any given sudoku board, assuming it is solvable, utilizing backtracking algorithm
'''


#0s represent empty spaces -- would have used # but that would require string / int conversions
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 6],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 8, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


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


def prettyBoard(startingBoard):
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
    if  len(startingBoard) != 9:
        print('Not enough rows in the board - expected 9, input {}'.format(len(startingBoard)))
        return False
    
    else:
        for i in range(9):
            if len(startingBoard[i]) != 9:
                print('Not enough columns in the board for row {} - expected 9, input {}'.format(i, len(startingBoard[i])))
                return False
            
            else:
                if (i % 3 == 0):
                    print('-------------')

                for j in range(9):
                    if (j % 3 == 0):
                        print('|', end = '')
                    
                    print(startingBoard[i][j], end = '')

                    if (j == 8):
                        print('|\n', end = '')

                if (i == 8):
                    print('-------------')


def findUnpopulated(startingBoard):
    '''should always be a 9 x 9 board, don't need to make range dynamic
    i = row number, j = column number'''
    for i in range(9):
        for j in range(9):
            if startingBoard[i][j] == 0:
                return(i, j)


def validatePosition(startingBoard, position, value):
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
        if startingBoard[x][i] == value and y != i: 
            return False
    
    #validate column
    #check each element (row) in column and see if equal to number that we are adding in (value). dont check for position that we just added value to
    for j in range(9):
        if startingBoard[j][y] == value and x != j: 
            return False


    #validate subgrid
    #can maybe use integer division on position parameter to determine subgrid -> posX // 3 & posY // 3   


    #all rules satisfied
    return True

#prettyBoard(board)

def tester(position):
    for section in subGrids:
        if position in section:
            gridSection = subGrids.index(section)
            #subGridValues = subGrids[gridSection]
            for subGridValue in subGrids[gridSection]:
                print(subGridValue)                
                #translate the subgrid positional values to corresponding numerical values in the starting board



tester((0,2))