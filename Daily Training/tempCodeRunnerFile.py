def convert_matrix_to_strings(H, W, A):
    result = []
    for i in range(H):
        row = ''
        for j in range(W):
            if A[i][j] == 0:
                row += '.'
            else:
                # 0-25 の範囲の数値を 'A'-'Z' に変換
                row += chr(ord('A') + A[i][j] - 1)
        result.append(row)
    return result

# 標準入力からの読み込み
import sys
input = sys.stdin.read
data = input().split()

H = int(data[0])
W = int(data[1])

A = []
index = 2
for i in range(H):
    row = []
    for j in range(W):
        row.append(int(data[index]))
        index += 1
    A.append(row)

# 行列を変換して出力
strings = convert_matrix_to_strings(H, W, A)
for s in strings:
    print(s)
