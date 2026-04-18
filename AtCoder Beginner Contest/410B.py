n, q = map(int, input().split())
x = list(map(int, input().split()))

boxes = [0] * n

result = []

for i in x:
    if i > 0:
        boxes[i - 1] += 1
        result.append(i)
    else:
        min_count = min(boxes)
        for j in range(n):
            if boxes[j] == min_count:
                boxes[j] += 1
                result.append(j + 1)
                break

print(" ".join(map(str, result)))
