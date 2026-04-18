import sys

Rt, Ct, Ra, Ca = map(int, sys.stdin.readline().split())
N, M, L = map(int, sys.stdin.readline().split())
S_comp = [sys.stdin.readline().split() for _ in range(M)]
T_comp = [sys.stdin.readline().split() for _ in range(L)]

move_map = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

r_diff = Rt - Ra
c_diff = Ct - Ca

count = 0
time = 0

s_ptr, t_ptr = 0, 0
s_char = S_comp[s_ptr][0]
s_rem = int(S_comp[s_ptr][1])
t_char = T_comp[t_ptr][0]
t_rem = int(T_comp[t_ptr][1])

while time < N:
    step = min(s_rem, t_rem)

    dr_s, dc_s = move_map[s_char]
    dr_t, dc_t = move_map[t_char]
    dr_d, dc_d = dr_s - dr_t, dc_s - dc_t

    if dr_d == 0 and dc_d == 0:
        if r_diff == 0 and c_diff == 0:
            count += step
    elif dr_d == 0:
        if r_diff == 0 and dc_d != 0 and -c_diff % dc_d == 0:
            k = -c_diff // dc_d
            if 1 <= k <= step:
                count += 1
    elif dc_d == 0:
        if c_diff == 0 and dr_d != 0 and -r_diff % dr_d == 0:
            k = -r_diff // dr_d
            if 1 <= k <= step:
                count += 1
    else:
        if -r_diff % dr_d == 0 and -c_diff % dc_d == 0:
            k1 = -r_diff // dr_d
            k2 = -c_diff // dc_d
            if k1 == k2 and 1 <= k1 <= step:
                count += 1

    r_diff += step * dr_d
    c_diff += step * dc_d
    time += step

    s_rem -= step
    t_rem -= step

    if s_rem == 0:
        s_ptr += 1
        if s_ptr < M:
            s_char, s_rem = S_comp[s_ptr][0], int(S_comp[s_ptr][1])

    if t_rem == 0:
        t_ptr += 1
        if t_ptr < L:
            t_char, t_rem = T_comp[t_ptr][0], int(T_comp[t_ptr][1])

print(count)
