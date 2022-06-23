n, m = int(input()), int(input())
matrix = [[''] * m for _ in range(n)]
max = -10000
result=[0, 0]
for row in range(n):
    temp = input().split(' ')
    for col in range(m):
        matrix[row][col] = temp[col]
for i in range(n):
    for j in range(m):
        if int(matrix[i][j]) > max:
            max = int(matrix[i][j])
            result[0] = i
            result[1] = j
print(*result)