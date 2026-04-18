from collections import Counter

N = int(input())
A = list(map(int, input().split()))

# j を真ん中に固定して考える

right = Counter(A)
left = Counter()

ans = 0

for a in A:
    right[a] -= 1

    if a % 5 == 0:
        t = a // 5
        a7 = 7 * t
        a3 = 3 * t

        # j が最大
        ans += left[a7] * left[a3]
        # j が最小
        ans += right[a7] * right[a3]

    left[a] += 1

print(ans)
