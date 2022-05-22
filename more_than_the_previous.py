from icecream import ic
num = input().split(' ')
result = []
for j in range(len(num)):
    result.append(int(num[j]))

count = 0
for i in range(1, len(result)):
    if result[i] > result[i - 1]:
        count += 1
print(count)