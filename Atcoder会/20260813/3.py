# すごい脳筋なんだけど

A = []

for _ in range(3):
    A.append(list(map(int, input().split())))

marked = [[False, False, False], [False, False, False], [False, False, False]]

N = int(input())

for _ in range(N):
    b = int(input())

    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                marked[i][j] = True

bingo = False

# 横
for i in range(3):
    if marked[i][0] and marked[i][1] and marked[i][2]:
        bingo = True

# 縦
for j in range(3):
    if marked[0][j] and marked[1][j] and marked[2][j]:
        bingo = True

# 斜め
if marked[0][0] and marked[1][1] and marked[2][2]:
    bingo = True

if marked[0][2] and marked[1][1] and marked[2][0]:
    bingo = True

if bingo:
    print("Yes")
else:
    print("No")
