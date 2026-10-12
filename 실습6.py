"""실습 6: 3×3 연립일차방정식을 크래머 공식으로 풂."""
from fractions import Fraction

A = [[1, -1, 1],
     [1, 1, -2],
     [1, 2, -1]]
b = [0, 1, 6]


def det3(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


if __name__ == '__main__':
    det_a = det3(A)
    print('A =', A)
    print('b =', b)
    print('det(A) =', det_a)
    if det_a == 0:
        print('det(A)=0이므로 크래머 공식으로 유일해를 구할 수 없습니다.')
    else:
        solutions = []
        for col in range(3):
            replaced = [[b[row] if j == col else A[row][j]
                         for j in range(3)] for row in range(3)]
            det_replaced = det3(replaced)
            solutions.append(Fraction(det_replaced, det_a))
            print(f'det(A{col + 1}) = {det_replaced}')
        for name, value in zip(('x', 'y', 'z'), solutions):
            print(f'{name} = {value}')
        print('검산 Ax =', [str(sum(A[i][j] * solutions[j] for j in range(3)))
                           for i in range(3)])
