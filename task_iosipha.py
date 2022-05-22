n, k = list(range(1,int(input()) + 1)), int(input())
if k == 1:
    print(n[-1])
else:
    while len(n) != 1:
        for i in range(k - 1):
            n.append(n[i])
        for j in range(k):
            n.pop(0)
    print(n[0])