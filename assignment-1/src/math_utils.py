def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    if gcd(a, m) != 1:
        return None

    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3

    return u1 % m

def determinant_3x3(matrix):
    return (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
            matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
            matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))

def matrix_minor(matrix, row, col):
    minor = []
    for i in range(len(matrix)):
        if i == row:
            continue
        minor_row = []
        for j in range(len(matrix[i])):
            if j == col:
                continue
            minor_row.append(matrix[i][j])
        minor.append(minor_row)
    return minor

def determinant_4x4(matrix):
    det = 0
    for col in range(4):
        minor = matrix_minor(matrix, 0, col)
        cofactor = ((-1) ** col) * matrix[0][col] * determinant_3x3(minor)
        det += cofactor
    return det

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result

def cofactor_matrix(matrix, mod):
    size = len(matrix)
    cofactors = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            minor = matrix_minor(matrix, i, j)
            minor_det = determinant_3x3(minor)
            cofactors[i][j] = ((-1) ** (i + j)) * minor_det

    return cofactors

def matrix_inverse(matrix, mod):
    det = determinant_4x4(matrix)
    det = det % mod

    if det < 0:
        det += mod

    det_inv = mod_inverse(det, mod)
    if det_inv is None:
        return None

    cofactors = cofactor_matrix(matrix, mod)
    adjugate = transpose(cofactors)

    inverse = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            inverse[i][j] = (det_inv * adjugate[i][j]) % mod
            if inverse[i][j] < 0:
                inverse[i][j] += mod

    return inverse

def matrix_multiply(matrix_a, matrix_b, mod):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = result[i][j] % mod

    return result
