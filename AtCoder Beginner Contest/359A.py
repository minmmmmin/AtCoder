N = int(input())

count = 0

for i in range(N):
    S = str(input())#for文のなかに入れちゃう。
    if S == "Takahashi":
        count += 1

print(count)