num = input().split(' ')
n = int(num[0])
m = int(num[1])
matrix = [['']*m for _ in range(n)]
count = 1
for i in range(n*m):
    for j in range(n):
        for y in range(m):
            if j+y == i:
                matrix[j][y] = str(count)
                count += 1
                break

for row in range(n):
    for col in range(m):
        print(matrix[row][col].ljust(3), end=' ')
    print()