N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
Good = 1
accept = 100000

for i in range(N):
  Ht = T - H[i]*0.006
  if (Ht - A)**2 <= accept:
    accept = (Ht - A)**2
    Good = i+1

print(Good)