import sys

t_str = sys.stdin.readline()
if t_str:
    t = int(t_str)
    for _ in range(t):
        n = int(sys.stdin.readline())
        s = sys.stdin.readline().strip()

        dp = [False] * (1 << n)
        dp[0] = True

        for mask in range(1, 1 << n):
            if s[mask - 1] == "1":
                continue

            for j in range(n):
                if (mask >> j) & 1:
                    prev_mask = mask ^ (1 << j)
                    if dp[prev_mask]:
                        dp[mask] = True
                        break

        if dp[(1 << n) - 1]:
            print("Yes")
        else:
            print("No")
