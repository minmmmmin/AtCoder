n = int(input())
mod = 998244353

inv2 = pow(2, mod - 2, mod)
sum_a = (((n % mod) * ((n + 1) % mod)) % mod * inv2) % mod

sum_d = 0
i = 1
while i <= n:
    val = n // i
    next_i = n // val + 1

    count = next_i - i

    term = (val % mod) * (count % mod)
    sum_d = (sum_d + term) % mod

    i = next_i

ans = (sum_a - sum_d + mod) % mod

print(ans)
