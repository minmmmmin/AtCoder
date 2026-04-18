from collections import deque

n = int(input())
A = [0] * (n + 1)
B = [0] * (n + 1)

need = [[] for _ in range(n + 1)]
learned = [False] * (n + 1)

for i in range(1, n + 1):
    a, b = map(int, input().split())
    A[i], B[i] = a, b
    if a != 0:
        need[a].append(i)
    if b != 0:
        need[b].append(i)

q = deque()
for i in range(1, n + 1):
    if A[i] == 0 and B[i] == 0:
        learned[i] = True
        q.append(i)

while q:
    cur = q.popleft()
    for nxt in need[cur]:
        if not learned[nxt]:
            if learned[A[nxt]] or learned[B[nxt]]:
                learned[nxt] = True
                q.append(nxt)

print(sum(learned))
