n = int(input())
ans = set()

for i in range(n):
    L = tuple(map(int, input().split()))
    ans.add(L)

print(len(ans))
