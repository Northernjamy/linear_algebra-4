def print_matrix(M):
    """계수 2열과 각 시스템의 상수항을 구분해 출력"""
    for row in M:
        print(
            f"[{row[0]:>3} {row[1]:>3}"
            f" | {row[2]:>3} | {row[3]:>3}]"
        )
    print()


# 첫 번째 시스템: x1 + 2x2 = 2, 3x1 + 7x2 = 8
# 두 번째 시스템: x1 + 2x2 = 1, 3x1 + 7x2 = 7
#
# 열의 의미: [x1 계수, x2 계수, 첫 번째 우변, 두 번째 우변]
M = [
    [1, 2, 2, 1],
    [3, 7, 8, 7],
]

print("1. 초기 첨가행렬")
print_matrix(M)

# 두 번째 행에서 첫 번째 행의 3배를 뺀다.
M[1] = [M[1][j] - 3 * M[0][j] for j in range(4)]

print("2. R2 ← R2 - 3R1")
print_matrix(M)

# 첫 번째 행에서 두 번째 행의 2배를 뺀다.
M[0] = [M[0][j] - 2 * M[1][j] for j in range(4)]

print("3. R1 ← R1 - 2R2")
print_matrix(M)

# 왼쪽이 단위행렬이 되었으므로 오른쪽 각 열이 해이다.
for system in range(2):
    column = 2 + system
    x1 = M[0][column]
    x2 = M[1][column]

    print(f"시스템 ({system + 1})의 해: x1 = {x1}, x2 = {x2}")
