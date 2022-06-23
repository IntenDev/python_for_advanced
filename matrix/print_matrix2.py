n, m = int(input()), int(input())
matrix = [['']*m for _ in range(n)]
for row in range(n):
    for col in range(m):
        matrix[row][col] = input()

for r in range(n):
    for c in range(m):
        print(matrix[r][c], end=' ')
    print()
print()
for r in range(m):
    for c in range(n):
        print(matrix[c][r], end=' ')
    print()