N = int(input())

pos_x = 0
pos_y = 0
now_time = 0

travel_success = True

for i in range(N):
    next_t,x,y = map(int,input().split())
    #かかる時間を考える、xを動かす回数とyを動かす回数と現時点での時間
    t_cost = abs(pos_x - x) + abs(pos_y - y) + now_time

    if next_t < t_cost:
        travel_success = False
        break
    #余裕があっても通り過ぎてから戻ってこれないと意味がない（奇数だとあかん）
    elif  (next_t - t_cost) % 2 != 0:
        travel_success = False
        break

    pos_x = x
    pos_y = y
    now_time = next_t

if travel_success:
    print("Yes")
else:
    print("No")

