num = int(input())
matrix = [['']*num for _ in range(num)]
result = 0
sum = 0
mid = 0
for row in range(num):
    temp = input().split(' ')
    for col in range(num):
        matrix[row][col] = int(temp[col])
        sum += int(temp[col])
    mid = sum / num
    for i in range(num):
        if mid < matrix[row][i]:
            result += 1
    print(result)
    sum = 0
    mid = 0
    result = 0