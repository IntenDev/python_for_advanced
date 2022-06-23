n, m = int(input()), int(input())
matrix = [[''] * m for i in range(n)]
for row in range(n):
    for col in range(m):
        matrix[row][col] = str(row*col).ljust(3)
for j in range(n):
    for y in range(m):
        print(matrix[j][y], end='')
    print()