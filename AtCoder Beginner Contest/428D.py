import sys
import math

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    C, D = map(int, input().split())
    ans = 0
    pow10 = [1] * 20
    for i in range(1, 20):
        pow10[i] = pow10[i - 1] * 10

    k = 1
    while True:
        lower_y_by_k = pow10[k - 1]
        upper_y_by_k = pow10[k] - 1
        lower_y_by_x = C + 1
        upper_y_by_x = C + D
        y_start = max(lower_y_by_k, lower_y_by_x)
        y_end = min(upper_y_by_k, upper_y_by_x)

        if y_start <= y_end:
            base = C * pow10[k]
            m2_low = base + y_start
            m2_high = base + y_end
            m_start = math.isqrt(m2_low)
            if m_start * m_start < m2_low:
                m_start += 1
            m_end = math.isqrt(m2_high)
            if m_start <= m_end:
                ans += m_end - m_start + 1

        if upper_y_by_k >= upper_y_by_x:
            break
        k += 1

    print(ans)
