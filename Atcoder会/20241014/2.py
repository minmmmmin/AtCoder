n=int(input())
b=list(map(int,input().split()))

a=[]
for i in range(2**n):
  a.append(b[i])
for j in range(0,(2**n-2)*2,2):
  if a[j]<a[j+1]:
    a.append(a[j+1])
  else:
    a.append(a[j])
if a[-1]>a[-2]:
  s=a[-2]
else:
  s=a[-1]
for l in range(len(b)):
  if s==b[l]:
    print(l+1)
    break