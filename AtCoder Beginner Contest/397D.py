import sys

def find_xy(N):
    # N の約数を一つずつ調べる
    for d in range(1, int(N**0.5) + 1):
        if N % d == 0:
            for y in range(1, int((N + 1) ** (1 / 3)) + 1):  # 適切な範囲で y を探索
                if 3 * y**2 * d + 3 * y * d**2 + d**3 == N:
                    return y + d, y  # x = y + d

            # N // d も約数なので同じ処理を行う
            if d != N // d:
                for y in range(1, int((N + 1) ** (1 / 3)) + 1):
                    if 3 * y**2 * (N // d) + 3 * y * (N // d)**2 + (N // d)**3 == N:
                        return y + (N // d), y

    return None

# 入力
N = int(sys.stdin.readline().strip())

# 結果
result = find_xy(N)
if result:
    print(result[0], result[1])
else:
    print(-1)
