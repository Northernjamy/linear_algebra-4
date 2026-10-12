"""실습 3: 여인수행렬과 수반행렬을 이용해 역행렬 계산."""
from fractions import Fraction

A = [[1, 2, 3],
     [2, 5, 3],
     [1, 0, 8]]


def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return sum(((-1) ** j) * matrix[0][j] * determinant(
        [[matrix[r][c] for c in range(n) if c != j] for r in range(1, n)])
        for j in range(n))


def minor(matrix, row, col):
    return [[matrix[r][c] for c in range(len(matrix)) if c != col]
            for r in range(len(matrix)) if r != row]


def print_matrix(title, matrix):
    print(title)
    for row in matrix:
        print(' ', '  '.join(f'{str(x):>5}' for x in row))
    print()


if __name__ == '__main__':
    det_a = determinant(A)
    print_matrix('원래 행렬 A:', A)
    print('det(A) =', det_a, '\n')
    if det_a == 0:
        print('행렬식이 0이므로 역행렬이 존재하지 않습니다.')
    else:
        n = len(A)
        cofactors = [[(-1) ** (i + j) * determinant(minor(A, i, j))
                      for j in range(n)] for i in range(n)]
        adjugate = [[cofactors[j][i] for j in range(n)] for i in range(n)]
        inverse = [[Fraction(value, det_a) for value in row] for row in adjugate]
        print_matrix('여인수행렬 C:', cofactors)
        print_matrix('수반행렬 adj(A) = C^T:', adjugate)
        print_matrix('A^(-1) = adj(A) / det(A):', inverse)
