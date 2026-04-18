Q = int(input())
bag = []
answers = []

for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        x = int(query[1])
        bag.append(x)
    else:
        m = min(bag)
        bag.remove(m)
        answers.append(m)

for a in answers:
    print(a)
