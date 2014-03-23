def sudoku_solved(sudoku):
	example = [1,2,3,4,5,6,7,8,9]
	flag = True
	for i in sudoku:
		if sorted(i) != example:
			return False
	for i in range(9):
		if sorted(get_column(sudoku,i)) != example:
			return False
	while i <= 6: 
		if sorted(get_square(sudoku,i,0)) != example:
			return False
		if sorted(get_square(sudoku,i,3)) != example:
			return False
		if sorted(get_square(sudoku,i,6)) != example:
			return False
		i+=3
	return True



def get_column(matrix,index):
    column = []
    for i in range(0,len(matrix)):
        column.append(matrix[i][index])
    return column

def get_square(matrix,row,column): #row,column - indexes of the first elemenr of the square
	square = []
	for i in range(3):
		for j in range(3):
			square.append(matrix[row + i][column + j])
	return square