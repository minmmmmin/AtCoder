N = int(input())
P = list(map(int, input().split()))

is_peak = [False] * N
is_valley = [False] * N

for i in range(1, N - 1):
    if P[i - 1] < P[i] > P[i + 1]:
        is_peak[i] = True
    if P[i - 1] > P[i] < P[i + 1]:
        is_valley[i] = True

peak_cum = [0] * (N + 1)
valley_cum = [0] * (N + 1)

for i in range(1, N + 1):
    peak_cum[i] = peak_cum[i - 1] + (1 if is_peak[i - 1] else 0)
    valley_cum[i] = valley_cum[i - 1] + (1 if is_valley[i - 1] else 0)

count = 0
for i in range(N):
    for r in range(i + 3, N + 1):
        peaks = peak_cum[r - 1] - peak_cum[i + 1]
        valleys = valley_cum[r - 1] - valley_cum[i + 1]

        if peaks == 1 and valleys == 1:
            if P[i] < P[i + 1]:
                count += 1

print(count)
