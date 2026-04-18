n = int(input())
p = list(map(int, input().split()))
for i in range(n):
    rank = 1
    for j in range(n):
        if p[j] > p[i]:
            rank += 1
    print(rank)
