h,w,x,y = map(int,input().split())

x -= 1
y -= 1

s = [input().strip() for _ in range(h)]

t = input().strip()

d = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}
# なんだよこれ…

house = set()
if s[x][y] == "@":
    house.add((x,y))

for i in t:
    dx,dy = d[i]
    nx,ny = x + dx, y+dy
    
    if 0 <= nx < h and 0 <= ny < w and s[nx][ny] != "#":
        x,y = nx,ny
        if s[x][y] == "@":
            house.add((x,y))

print(f"{x + 1} {y + 1}",len(house))