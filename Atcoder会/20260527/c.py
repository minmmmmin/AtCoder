N,A,B=map(int,input().split())

for i in range(1,N+1):
    if i%2==1:
        for a in range(1,A+1):
            ans=""
            for j in range(1,N+1):
                if j%2==1:
                    ans+="."*B
                else:
                    ans+="#"*B
            print(ans)
    else:
        for a in range(1,A+1):
            ans=""
            for j in range(1,N+1):
                if j%2==1:
                    ans+="#"*B
                else:
                    ans+="."*B
            print(ans)
