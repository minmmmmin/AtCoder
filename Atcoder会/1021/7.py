from functools import lru_cache

@lru_cache(maxsize = None)
def f(N):
    if N == 1:
        return 0
    else:
        return f(N // 2) + f((N + 1) // 2) + N

print(f(int(input())))
