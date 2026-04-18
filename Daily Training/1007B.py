N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

#一番重い荷物を計算すればよくねーかの気持ち

m = [0]*(N+1)

for i in range(N):
    m[A[i]] = max(m[A[i]],W[i])
     
result = sum(W) - sum(m)

print(result)