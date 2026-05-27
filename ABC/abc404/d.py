from itertools import product

N, M = map(int, input().split())
C = list(map(int, input().split()))

ahoanimal_zoo = [[] for _ in range(M)]
for i in range(M):
    data = list(map(int, input().split()))
    K = data[0]
    A = data[1:]
    for zoo in A:
        ahoanimal_zoo[i].append(zoo - 1)

ans = float("inf")

for visit_pattern in product((0, 1, 2), repeat=N):
    animal_count = [0] * M

    for zoo_index in range(N):
        times = visit_pattern[zoo_index]
        if times == 0:
            continue
        for ahoanimal_index in range(M):
            if zoo_index in ahoanimal_zoo[ahoanimal_index]:
                animal_count[ahoanimal_index] += times

    if all(count >= 2 for count in animal_count):
        cost = sum(C[i] * visit_pattern[i] for i in range(N))
        ans = min(ans, cost)

print(ans)
