num = input().split(' ')
n = int(num[0])
m = int(num[1])
matrix = [['']*m for _ in range(n)]
b, c = 0, 0
while b < n*m:
    for i in range(c, n):
        for j in range(m):
            b += 1
            matrix[i][j] = str(b)
        c += 1
        break

    for x in range(c, n):
        for y in range(m-1, -1, -1):
            b +=1
            matrix[x][y] = str(b)
        c += 1
        break
for row in range(n):
    for col in range(m):
        print(matrix[row][col].ljust(3), end=' ')
    print()

