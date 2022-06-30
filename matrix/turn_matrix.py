n = int(input())
matrix = [['']*n for _ in range(n)]
result = [['']*n for _ in range(n)]

for row in range(n):
    temp = input().split(' ')
    for col in range(n):
        matrix[row][col] = temp[col]

t = n-1
for i in range(n):
    for j in range(n):
        result[i][j] = matrix[t][i]
        t -= 1
    t = n-1

for r in range(n):
    for c in range(n):
        print(result[r][c], end=' ')
    print()