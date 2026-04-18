x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = map(int, input().split())

vec_ab = [x2 - x1, y2 - y1]
vec_bc = [x3 - x2, y3 - y2]
vec_cd = [x4 - x3, y4 - y3]
vec_da = [x1 - x4, y1 - y4]

cross_ab_bc = vec_ab[0] * vec_bc[1] - vec_ab[1] * vec_bc[0]
cross_bc_cd = vec_bc[0] * vec_cd[1] - vec_bc[1] * vec_cd[0]
cross_cd_da = vec_cd[0] * vec_da[1] - vec_cd[1] * vec_da[0]
cross_da_ab = vec_da[0] * vec_ab[1] - vec_da[1] * vec_ab[0]

if cross_ab_bc > 0 and cross_bc_cd > 0 and cross_cd_da > 0 and cross_da_ab > 0:
    print("Yes")
elif cross_ab_bc < 0 and cross_bc_cd < 0 and cross_cd_da < 0 and cross_da_ab < 0:
    print("Yes")
else:
    print("No")
