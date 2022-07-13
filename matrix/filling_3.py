n = int(input())
matrix = [[0]*n for _ in range(n)]
for i in range(n):
    matrix[i][i], matrix[i][n-i-1] = 1, 1
for j in range(n):
    for x in range(n):
        print(matrix[j][x], end=' ')
    print()

