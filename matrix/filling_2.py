num = input().split(' ')
n = int(num[0])
m = int(num[1])
matrix = [['']*m for _ in range(n)]
x = 1
for i in range(m):
    for j in range(n):
        matrix[j][i] = str(x)
        x += 1
for r in range(n):
    for c in range(m):
        print(matrix[r][c].ljust(3), end=' ')
    print()