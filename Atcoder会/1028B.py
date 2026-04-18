n = int(input())
p = list(map(int,input().split()))

for i in range(0,n):
    ans = (max,p[n]-p[0]+1)
    
print(ans)

#ぼつ
if(max(p) == p[0] and len(p)== len(set(p))):
    print(0)
else:
    print(max(p)+1 - p[0])