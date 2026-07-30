N,K = map(int,input().split())
S = input()

import more_itertools

ans = 0
for ptr in more_itertools.distinct_permutations(S):
    for i in range(N-K+1):
        if ptr[i:i+K] == ptr[i:i+K][::-1]:
            break
    else:
        ans += 1
print(ans)