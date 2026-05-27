N, K= map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0

for i in range(N-1):
    if abs(A[i] - A[i+1]) < K:
        ans = True
    elif abs(A[i] - B[i+1]) < K:
        ans = True
    else:
        ans = False
    
    if abs(B[i] - A[i+1]) < K:
        ans = True
    elif abs(B[i] - B[i+1]) < K:
        ans = True
    else:
        ans = False
    
    if ans:
        count += 1

if count == N-1:
    print("Yes")
else:
    print("No")