import numpy as np

sudokuBoard = []
print ('Please enter the 9X9 Sudoku board to solve. Use \'-\' to denote blank spaces. ')
print ('Enter the board one row after the other ')

for i in range (0, 9):
    temporaryList = list(input().split())
    if len(temporaryList) != 9:
        print ('Your input row did not have 9 elements. Please check your input. ')
        exit(True)
    sudokuBoard.append(temporaryList)

print('The Sudoku Board before solving: \n')
print(np.matrix(sudokuBoard))

def checkRow ( position_X, position_Y, number ):
    """
        This function iterates over the row of the said position and checks if 
        a number equal to the passed number already exists 
    """
    for i in range (0, len(sudokuBoard[0])):
        if sudokuBoard[position_X][i] == number and i != position_Y:
            return False
    return True

def checkColumn ( position_X, position_Y, number ):
    """
        This function iterates over the column of the said position and checks if
        a number equal to the passed number already exists
    """
    for i in range (0, len(sudokuBoard)):
        if sudokuBoard[i][position_Y] == number and i != position_X:
            return False
    return True

def checkGrid ( position_X, position_Y, number ):
    """
        This function checks whether the given number is already present in the grid
    """
    grid_X = position_X // 3
    grid_Y = position_Y // 3

    grid_XStart = grid_X * 3
    grid_YStart = grid_Y * 3
    grid_Xlimit = grid_XStart + 3
    grid_Ylimit = grid_YStart + 3

    for i in range ( grid_XStart, grid_Xlimit ):
        for j in range ( grid_YStart, grid_Ylimit ):
            if sudokuBoard[i][j] == number and i != position_X and j != position_Y:
                return False
    return True

def isPositionValid ( position_X, position_Y, number ):
    """
        This is a function which checks the whether the number can fit into the position 
        It checks whether its in the same row, same column or same grid
    """
    if checkRow(position_X, position_Y, number) and checkColumn(position_X, position_Y, number) and checkGrid(position_X, position_Y, number):
        return True
    return False

def Solver():
    """ 
        This is the main solver program that we'd call recursively
    """
    finish = True
    for i in range (0, len(sudokuBoard)):
        for j in range (0, len(sudokuBoard[0])):
            if sudokuBoard[i][j] == '-':
                finish = False
                break
        if finish == False:
            break

    if finish:
        return True

    position_X = i
    position_Y = j

    for i in range (1, 10):
        if isPositionValid ( position_X, position_Y, str(i)):
            sudokuBoard[position_X][position_Y] = str(i)
    
            if Solver():
                return True
        
            sudokuBoard[position_X][position_Y] = '-'

    return False

Solver()
print ('\n The Sudoku Board after solving: \n')
print (np.matrix(sudokuBoard))
