N = int(input())

loss = 0

for _ in range(N):
    A, B, S = input().split()
    A = int(A)
    B = int(B)

    if S == "keep":
        loss += B - A

print(loss)
