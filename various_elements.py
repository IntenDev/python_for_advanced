from icecream import ic
num = [int(i) for i in input().split(' ')]
cnt = 1
for j in range(1, len(num)):
    if num[j] != num[j - 1]:
        cnt += 1
print(cnt)