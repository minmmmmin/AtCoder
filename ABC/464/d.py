# これってあのセレステですか？？？
# 私はDPを履修したんですよ

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    S = input().strip()
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))

    if S[0] == "S":
        dpS = 0
        dpR = -X[0]
    else:
        dpS = -X[0]
        dpR = 0

    for i in range(1, N):
        if S[i] == "S":
            costS = 0
            costR = -X[i]
        else:
            costS = -X[i]
            costR = 0

        nextS = max(dpS, dpR + Y[i - 1]) + costS
        nextR = max(dpS, dpR) + costR

        dpS = nextS
        dpR = nextR

    print(max(dpS, dpR))
