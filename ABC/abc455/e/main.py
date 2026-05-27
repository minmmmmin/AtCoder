# 全体から引きたいよね

from collections import defaultdict

N = int(input())
S = input()

total = N * (N + 1) // 2

cntA = cntB = cntC = 0

ab = defaultdict(int)
bc = defaultdict(int)
ca = defaultdict(int)
abc = defaultdict(int)

ab[0] += 1
bc[0] += 1
ca[0] += 1
abc[(0, 0)] += 1

same_ab = 0
same_bc = 0
same_ca = 0
same_abc = 0

for ch in S:
    if ch == "A":
        cntA += 1
    elif ch == "B":
        cntB += 1
    else:
        cntC += 1

    d_ab = cntA - cntB
    d_bc = cntB - cntC
    d_ca = cntC - cntA

    same_ab += ab[d_ab]
    same_bc += bc[d_bc]
    same_ca += ca[d_ca]

    key = (cntA - cntB, cntA - cntC)
    same_abc += abc[key]

    ab[d_ab] += 1
    bc[d_bc] += 1
    ca[d_ca] += 1
    abc[key] += 1

# print(same_ab)

bad = same_ab + same_bc + same_ca - 2 * same_abc

ans = total - bad
print(ans)