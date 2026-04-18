N = int(input())
A = int(input())

for i in range(1,N + 1):
    C,B = input().split()
    B = int(B)
    if C == "+":
        print(i,A + B)
        A += B
    elif C == "-":
        print(i,A - B)
        A -= B
    elif C == "*":
        print(i,A * B)
        A *= B
    elif C == "/" :
        if B != 0:
            print(i,A//B)
            A //= B
        else:
            print("error")
            break

            
