N = int(input())
S = input().strip()

posA = []
for i in range(len(S)):
    if S[i] == "A":
        posA.append(i)

target1 = []
for i in range(N):
    target1.append(2 * i)

cost1 = 0
for j in range(N):
    p = posA[j]
    t = target1[j]
    cost1 += abs(p - t)

target2 = []
for i in range(N):
    target2.append(2 * i + 1)

cost2 = 0
for j in range(N):
    p = posA[j]
    t = target2[j]
    cost2 += abs(p - t)

if cost1 < cost2:
    print(cost1)
else:
    print(cost2)
