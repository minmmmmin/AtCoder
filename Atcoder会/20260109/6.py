N = int(input())
A = sorted(int(x) for x in input().split())

result = sum(A) * (N - 1)

print(result)

j = N - 1
for i in range(N):
    while i < j and A[i] + A[j] >= 10**8:
        j -= 1
    result -= (N - 1 - max(i, j)) * 10**8
    # print(result)
print(result)
