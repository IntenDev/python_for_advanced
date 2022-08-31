num = input().split(' ')
n = int(num[0])
m = int(num[1])
matrix = [['']*m for _ in range(n)]
count = 1
for x in range(n):
    for y in range(m):
        if count > m:
            count = 1
        if x != 0 and y == 0 and count != m:
            count = (matrix[x-1][y]) + 1
        elif x != 0 and y == 0 and count == m:
            count = 1
        matrix[x][y] = count
        count += 1

for row in range(n):
    for col in range(m):
        print(matrix[row][col], end=' ')
    print()
