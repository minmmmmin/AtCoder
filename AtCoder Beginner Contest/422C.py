T = int(input())
for _ in range(T):
    nA, nB, nC = map(int, input().split())
    ans = min(nA, nC, (nA + nB + nC) // 3)
    print(ans)
