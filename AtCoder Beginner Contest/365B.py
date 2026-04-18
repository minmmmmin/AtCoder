import numpy as np

A = int(input())

B = list(map(int, input().split()))

first = 0
second = 0
first_index = 0
second_index = 0


for i in range (len(B)):
    if B[i] > first:
        second = first
        second_index = first_index
        first = B[i]
        first_index = i
    elif B[i] > second:
        second = B[i]
        second_index = i

print(second_index + 1)