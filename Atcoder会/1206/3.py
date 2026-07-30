from itertools import permutations

n,m = map(int,input().split())

S = [input() for i in range(n)]

list = list(permutations(S))

print(list)

for p in permutations(range(m)):
    