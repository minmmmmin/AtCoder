A,B,C,D = map(int,input().split())

if A==B==C==D:
    print("No")
elif A==B==C or A==B==D or A==C==D or B==C==D or (A==B and C==D) or (A==C and B==D) or (A==D and C==B):
    print("Yes")
else:
    print("No")
