N = int(input())
A = list(map(int, input().split()))

ans = set(A)

if N == len(ans):
    print("YES")
else:
    print("NO")
