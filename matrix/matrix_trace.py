num = int(input())
matrix = [['']*num for _ in range(num)]
result = 0
for row in range(num):
    temp = input().split(' ')
    for col in range(num):
        matrix[row][col] = temp[col]

for i in range(num):
    result += int(matrix[i][i])
print(result)