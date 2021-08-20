def sparse_matrix_multiplication(matrix_a, matrix_b):
    
    # error if rows / cols do not match
    if len(matrix_a[0]) != len(matrix_b):
        return [[]]

    sparse_a = get_dictionary_of_nonzero_cells(matrix_a)
    sparse_b = get_dictionary_of_nonzero_cells(matrix_b)
    
    matrix_c = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]

    # iterate keys of sparse_a
    for i, k in sparse_a.keys():
        # iterate through # of cols
        for j in range(len(matrix_b[0])):
            if (k, j) in sparse_b.keys():
                matrix_c[i][j] += sparse_a[(i,k)] * sparse_b[(k,j)]

    return matrix_c

def get_dictionary_of_nonzero_cells(matrix):
    nonzero_dict = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                nonzero_dict[(i,j)] = matrix[i][j]
    
    return nonzero_dict


matrix_a = [[0, 2, 0], [0, -3, 5]]
matrix_b = [[0, 10, 0], [0, 0, 0], [0, 0, 4]]

C = sparse_matrix_multiplication(matrix_a, matrix_b)
print(C)