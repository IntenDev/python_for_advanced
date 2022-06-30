n = int(input())
matrix = [['']*n for _ in range(n)]

for row in range(n):
    temp = input().split(' ')
    for col in range(n):
        matrix[row][col] = temp[col]

for i in range(n // 2):
    for j in range(n):
        matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]

for r in range(n):
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()