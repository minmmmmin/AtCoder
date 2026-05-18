a,b,c,d=map(int,input().split())
ans=max(0,min(b,d)-max(a,c))
if ans<0:
    print(0)
else:
    print(ans)