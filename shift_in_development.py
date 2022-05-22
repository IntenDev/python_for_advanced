num = [int(i) for i in input().split(' ')]
num.insert(0, num[len(num)-1])
num.pop(len(num) - 1)
print(*num)