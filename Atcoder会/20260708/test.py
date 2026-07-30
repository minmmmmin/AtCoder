def getMinOperations(arr):
    n = len(arr)
    ans = 0

    for i in range(32):
        ones = 0

        for j in arr:
            if (j >> i) & 1:
                ones += 1
        zeros = n - ones
        ans += min(ones, zeros)

    return ans
