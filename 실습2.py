"""실습 2: 행 연산으로 역행렬 존재 여부를 판정."""
from fractions import Fraction

A = [[1, -3, 4],
     [2, -5, 7],
     [0, -1, 1]]


def rref_and_rank(matrix):
    result = [[Fraction(value) for value in row] for row in matrix]
    rows, cols = len(result), len(result[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if result[r][col] != 0), None)
        if pivot is None:
            continue
        result[pivot_row], result[pivot] = result[pivot], result[pivot_row]
        factor = result[pivot_row][col]
        result[pivot_row] = [x / factor for x in result[pivot_row]]
        for r in range(rows):
            if r != pivot_row:
                multiplier = result[r][col]
                result[r] = [result[r][j] - multiplier * result[pivot_row][j]
                             for j in range(cols)]
        pivot_row += 1
        if pivot_row == rows:
            break
    return result, pivot_row


if __name__ == '__main__':
    print('원래 행렬 A:')
    for row in A:
        print(row)
    reduced, rank = rref_and_rank(A)
    print('\n행 연산 후 기약 행 사다리꼴(RREF):')
    for row in reduced:
        print([str(v) for v in row])
    print(f'\nrank(A) = {rank}, 행렬 크기 = {len(A)}')
    if rank == len(A):
        print('판정: 역행렬이 존재합니다.')
    else:
        print('판정: 역행렬이 존재하지 않습니다. (행이 선형종속)')
