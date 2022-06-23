n, m = int(input()), int(input())
matrix = [['']*m for _ in range(n)]
for row in range(n):
    for col in range(m):
        matrix[row][col] = input()

for r in range(n):
    for c in range(m):
        print(matrix[r][c], end=' ')
    print()