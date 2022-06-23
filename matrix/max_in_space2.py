num = int(input())
matrix = [['']*num for _ in range(num)]
result = -10000

for row in range(num):
    temp = input().split(' ')
    for col in range(num):
        matrix[row][col] = temp[col]

for i in range(num):
    for j in range(num):
        if i >= j and i < num - 1 -j or i <= j and i > num-1-j:
            if int(matrix[i][j]) > result:
                result = int(matrix[i][j])
        if int(matrix[i][i]) > result:
            result = int(matrix[i][i])
        if int(matrix[i][num - i - 1]) > result:
            result = int(matrix[i][num - i - 1])
print(result)