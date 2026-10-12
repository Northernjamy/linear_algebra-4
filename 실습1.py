"""실습 1: 기본 행 연산(가우스-조르당 소거법)으로 역행렬 계산."""
from fractions import Fraction

A = [[1, 2, 3],
     [2, 5, 3],
     [1, 0, 8]]


def print_matrix(matrix, title):
    print(title)
    for row in matrix:
        print('  ', '  '.join(f'{str(x):>5}' for x in row))
    print()


def inverse_by_row_operations(matrix):
    n = len(matrix)
    # [A | I] 형태의 확대행렬
    aug = [[Fraction(matrix[i][j]) for j in range(n)]
           + [Fraction(int(i == j)) for j in range(n)] for i in range(n)]

    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col] != 0), None)
        if pivot is None:
            raise ValueError('역행렬이 존재하지 않습니다.')
        aug[col], aug[pivot] = aug[pivot], aug[col]

        divisor = aug[col][col]
        aug[col] = [v / divisor for v in aug[col]]

        for r in range(n):
            if r != col:
                factor = aug[r][col]
                aug[r] = [aug[r][j] - factor * aug[col][j]
                          for j in range(2 * n)]
    return [row[n:] for row in aug]


if __name__ == '__main__':
    print_matrix(A, '원래 행렬 A:')
    inverse = inverse_by_row_operations(A)
    print_matrix(inverse, '행 연산으로 구한 역행렬 A^(-1):')
