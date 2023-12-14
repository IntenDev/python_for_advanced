# def s(a, *vs, b=10):
#    res = a + b
#    for v in vs:
#        res += v
#    return res
#
# print(s(21))

a, b = map(int, input().split())

def C(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return C(n-1, k) + C(n-1, k-1)

y = C(a, b)
print(y)