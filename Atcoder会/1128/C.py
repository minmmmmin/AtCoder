N, A = map(int, input().split())
T = list(map(int, input().split()))


print(A + T[0])

now_time = A + T[0]

for i in range(1, N):
    if T[i] - T[i - 1] <= A:
        print(now_time + A)
        now_time += A
    else:
        print(T[i] + A)
        now_time = T[i] + A
