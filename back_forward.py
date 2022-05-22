str_num = input().split(' ')
result = []
for i in range(len(str_num)):
    result.append(int(str_num[i]))

for j in range(1, len(result), 2):
    result[j-1], result[j] = result[j], result[j-1]

print(*result)