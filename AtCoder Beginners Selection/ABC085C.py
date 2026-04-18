N,Y = map(int,input().split())

count = 0

def bill_combination(N, Y):
    for i in range(N+1):
        for j in range(N+1-i):
            k = N - i - j
            if 10000*i+5000*j+1000*k == Y:
                return i,j,k
    return -1,-1,-1

i,j,k = bill_combination(N, Y)

print(i,j,k)