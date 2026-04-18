n = int(input())

S = list(map(int,input().split()))
ans = 0
m = S[0]

for j in range (n):
    if m >= S[j]:
        ans += 1
        m = min(S[j], m)
        
print(ans)
        
        