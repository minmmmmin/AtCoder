# クソでかい数からこれが通るかなー？ってみていくのがいいのかな
n, k = map(int, input().split())
a = list(map(int, input().split()))

ok = 0
ng = 10**19 # クソでかい数

while ng - ok > 1:
    mid = (ok + ng) // 2
    # print(mid)

    need = 0

    for i in range(n):
        if a[i] < mid:
            # 必要操作回数を計算
            need += (mid - a[i] + i) // (i + 1)

    # 使いきっちゃったらだめだよ
    if need <= k:
        ok = mid
    else:
        ng = mid
    # print(ok)

print(ok)