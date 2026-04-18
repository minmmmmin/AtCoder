"""A, B = input().split()

A = int(A)
B = int(B)"""

#これを綺麗にするのがmap
A, B = map(int,input().split())
print(A+B)