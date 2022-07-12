num = input().split(' ')
n = int(num[0])
m = int(num[1])
matrix = [['']*m for _ in range(n)]
for c in range(n):
    for r in range(m):
        if c % 2 == 0 and r % 2 == 0 or c % 2 != 0 and r % 2 != 0:
            matrix[c][r] = '.'
        if c % 2 != 0 and r % 2 == 0 or c % 2 == 0 and r % 2 != 0:
            matrix[c][r] = '*'
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()