n, m = int(input()), int(input())
matrix = [['']*m for _ in range(n)]

for row in range(n):
    temp = input().split(' ')
    for col in range(m):
        matrix[row][col] = temp[col]

temp = input().split(' ')
c1, c2 = int(temp[0]), int(temp[1])

for i in range(n):
    for j in range(m):
        if j == c1:
            matrix[i][c1], matrix[i][c2] = matrix[i][c2], matrix[i][c1]
for r in range(n):
    for c in range(m):
        print(matrix[r][c], end=' ')
    print()

