N = int(input())
a = set()

for i in range(2,N):
    
    if pow(i,2) > N:
        break
    for j in range(2,N):
        z = pow(i,j)
        if z <= N:
            a.add(z)
        else:
            break
        
print(N - len(a))