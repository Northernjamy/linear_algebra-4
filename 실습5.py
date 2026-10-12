"""실습 5: 2×2 연립일차방정식을 크래머 공식으로 풂."""
from fractions import Fraction

A = [[3, -2],
     [-5, 4]]
b = [6, 8]


def det2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


if __name__ == '__main__':
    det_a = det2(A)
    print('A =', A)
    print('b =', b)
    print('det(A) =', det_a)
    if det_a == 0:
        print('det(A)=0이므로 크래머 공식으로 유일해를 구할 수 없습니다.')
    else:
        a1 = [[b[0], A[0][1]], [b[1], A[1][1]]]
        a2 = [[A[0][0], b[0]], [A[1][0], b[1]]]
        det_a1, det_a2 = det2(a1), det2(a2)
        x = Fraction(det_a1, det_a)
        y = Fraction(det_a2, det_a)
        print('det(A1) =', det_a1)
        print('det(A2) =', det_a2)
        print('x = det(A1) / det(A) =', x)
        print('y = det(A2) / det(A) =', y)
