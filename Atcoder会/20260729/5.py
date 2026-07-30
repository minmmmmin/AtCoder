# いもすをしらない
N = int(input())
A = list(map(int, input().split()))

m = max(A)

cnt = [0] * (m + 1)

for x in A:
    cnt[x] += 1

digits = []
carry = 0
now = N

# 10^0 の位から順番に計算する
for i in range(m):
    carry += now

    digits.append(str(carry % 10))
    carry //= 10
    now -= cnt[i + 1]

while carry > 0:
    digits.append(str(carry % 10))
    carry //= 10

print("".join(reversed(digits)))