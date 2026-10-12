"""실습 4: 역행렬을 이용하여 연립일차방정식 Ax=b를 풂."""
from fractions import Fraction

A = [[1, 2, 3],
     [1, 3, 6],
     [2, 6, 13]]
b = [1, 3, 5]


def inverse_by_row_operations(matrix):
    n = len(matrix)
    aug = [[Fraction(matrix[i][j]) for j in range(n)]
           + [Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col] != 0), None)
        if pivot is None:
            raise ValueError('A는 역행렬이 없어 이 방법으로 풀 수 없습니다.')
        aug[col], aug[pivot] = aug[pivot], aug[col]
        factor = aug[col][col]
        aug[col] = [x / factor for x in aug[col]]
        for r in range(n):
            if r != col:
                factor = aug[r][col]
                aug[r] = [aug[r][j] - factor * aug[col][j] for j in range(2 * n)]
    return [row[n:] for row in aug]


if __name__ == '__main__':
    a_inverse = inverse_by_row_operations(A)
    x = [sum(a_inverse[i][j] * b[j] for j in range(len(b)))
         for i in range(len(b))]
    print('A =')
    for row in A:
        print(row)
    print('b =', b)
    print('\nA^(-1) =')
    for row in a_inverse:
        print([str(v) for v in row])
    print('\nx = A^(-1)b =', [str(v) for v in x])
    print('검산 Ax =', [str(sum(A[i][j] * x[j] for j in range(len(x))))
                       for i in range(len(x))])
