N, Q = map(int, input().split())
queries = []
for i in range(Q):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    queries.append((a, b, i))

queries.sort()

ans = [""] * Q
stack = []

for a, b, idx in queries:
    while stack and stack[-1] < a:
        stack.pop()
    if stack and stack[-1] < b:
        ans[idx] = "No"
    else:
        ans[idx] = "Yes"
        stack.append(b)

print("\n".join(ans))
