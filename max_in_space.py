num = int(input())
matrix = [['']*num for _ in range(num)]
result = -10000

for row in range(num):
    temp = input().split(' ')
    for col in range(num):
        matrix[row][col] = temp[col]

for i in range(1, num + 1):
    for j in range(i):
        if int(matrix[i-1][(i-1)-j]) > result:
            result = int((matrix[i-1][(i-1)-j]))
print(result)