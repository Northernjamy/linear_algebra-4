from fractions import Fraction


def print_matrix(M):
    """첨가행렬 출력"""
    for row in M:
        left = " ".join(f"{str(v):>5}" for v in row[:-1])
        print(f"[{left} | {str(row[-1]):>5}]")
    print()


# 연립방정식
#  x1 - 2x2 +  x3 =  0
#       2x2 - 8x3 =  8
# -4x1 + 5x2 + 9x3 = -9

M = [
    [1, -2, 1, 0],
    [0, 2, -8, 8],
    [-4, 5, 9, -9],
]

# 분수를 정확하게 계산하기 위한 변환
M = [[Fraction(v) for v in row] for row in M]

print("1. 초기 첨가행렬")
print_matrix(M)

# 세 번째 행의 x1 계수를 0으로 만든다.
M[2] = [M[2][j] + 4 * M[0][j] for j in range(4)]

print("2. R3 ← R3 + 4R1")
print_matrix(M)

# 두 번째 행의 피벗을 1로 만든다.
M[1] = [v / 2 for v in M[1]]

print("3. R2 ← R2 / 2")
print_matrix(M)

# 세 번째 행의 x2 계수를 0으로 만든다.
M[2] = [M[2][j] + 3 * M[1][j] for j in range(4)]

print("4. R3 ← R3 + 3R2 : 삼각형 형태 완성")
print_matrix(M)

# 후진 대입: 마지막 방정식부터 역순으로 계산
n = 3
x = [Fraction(0) for _ in range(n)]

print("5. 후진 대입")

for i in range(n - 1, -1, -1):
    known = sum(M[i][j] * x[j] for j in range(i + 1, n))
    x[i] = (M[i][-1] - known) / M[i][i]
    print(f"x{i + 1} = {x[i]}")

print("최종 결과")
for i, value in enumerate(x, start=1):
    print(f"x{i} = {value}")
