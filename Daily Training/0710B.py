import sys
input = sys.stdin.read
N = int(input().strip())

result = str(N).zfill(4)

# 方法2: formatメソッドを使う
# result = "{:04d}".format(N)

print(result)
