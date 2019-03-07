def reverse(x):
    res, remaining = 0, abs(x)
    while remaining:
        res = res * 10 + remaining % 10
        # print res
        remaining //= 10
        # print remaining

    return -res if x < 0 else res


reverse(1234)
