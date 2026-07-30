n = int(input())
lr = sorted([list(map(int,input().split())) for _ in range(n)])

# print(lr)

ans = [lr[0]]
# print(lr[0][1])
for l,r in lr[1:]:
    if l<=ans[-1][1]:
        ans[-1][1]=max(ans[-1][1],r)
    else:
        ans.append([l,r])

for i in ans:
    print(*i)
