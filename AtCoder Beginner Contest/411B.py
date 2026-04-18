N = int(input())
D = list(map(int, input().split()))

positions = [0]
for dist in D:
    positions.append(positions[-1] + dist)

for i in range(N - 1):
    result = []
    for j in range(i + 1, N):
        result.append(str(positions[j] - positions[i]))
    print(" ".join(result))
