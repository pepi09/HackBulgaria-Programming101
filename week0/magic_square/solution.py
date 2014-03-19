from functools import reduce
def magic_square(matrix):
    sum = reduce(add,matrix[0])
    for i in range(0,len(matrix)):
        if sum != reduce(add,matrix[i]):
            return False
    for i in range(0,len(matrix)):
        if sum != reduce(add,get_column(matrix,i)):
            return False
    diagonal = []
    back_diagonal = []
    j = 0
    for i in range(0,len(matrix)):
        diagonal.append(matrix[i][j])
        back_diagonal.append(matrix[len(matrix)-i-1][len(matrix)-j-1])
        j+=1

    if reduce(add,matrix[0]) != sum and reduce(add,matrix[0]) != sum:
        return False
    return True


def add(x,y):
    return x + y

def get_column(matrix,index):
    column = []
    for i in range(0,len(matrix)):
        column.append(matrix[i][index])
    return column
