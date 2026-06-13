N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(N):
    axe = A[i]
    owner = B[axe - 1]

    if owner != i + 1:
        print("No")
        break
else:
    print("Yes")