def matrix_addition(matrix1, matrix2):
    result = []
    
    for i in range(len(matrix1)):
        row_result = []
        for j in range(len(matrix1[i])):
            sum_element = matrix1[i][j] + matrix2[i][j]
            row_result.append(sum_element)
        result.append(row_result)
    
    return result

matrix_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result_matrix = matrix_addition(matrix_A, matrix_B)

for row in result_matrix:
    print(row)