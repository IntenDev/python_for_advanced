n = int(input())
matrix = [['']*n for _ in range(n)]
for z in range(n):
    matrix[z][n - z - 1] = 1
for i in range(n):
    for j in range(n):
        if j < (n-i-1):
            matrix[i][j] = 0
        if j > (n-i-1):
            matrix[i][j] = 2
for row in range(n):
    for col in range(n):
        print(matrix[row][col], end=' ')
    print()