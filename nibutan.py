A, B, X = map(int, input().split())

# 探索したい整数の範囲を定義
left = 0
right = 10**9 + 1


# 満たすべき条件
def validate(arg):
    if (A * arg) + (B * (len(str(arg)))) <= X:
        return True


# 条件を満たす最大整数を探す二分探索
max_int = 0
while abs(right - left) > 1:
    mid = (left + right) // 2
    if validate(mid):
        max_int = mid
        left = mid
    else:
        right = mid

print(max_int)
