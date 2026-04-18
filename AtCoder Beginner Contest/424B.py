N, M, K = map(int, input().split())

solved = [set() for _ in range(N + 1)]
output = set()
ans = []

for _ in range(K):
    a, b = map(int, input().split())
    solved[a].add(b)

    if len(solved[a]) == M and a not in output:
        ans.append(a)
        output.add(a)

print(" ".join(map(str, ans)))
