n = int(input())
m = int(input())
mult = [[' '] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        mult[i][j] = str(i*j)

for row in range(n):
    for col in range(m):
        print(mult[row][col].ljust(3), end=' ')
    print()