def transpose(matrix):
    n = len(matrix)       
    m = len(matrix[0])   

    transposed = []
    for j in range(m):
        new_row = []
        for i in range(n):
            new_row.append(matrix[i][j]) 
        transposed.append(new_row)

    matrix[:] = transposed
