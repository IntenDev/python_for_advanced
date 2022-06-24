n = int(input())
matrix = [[''] * n for _ in range(n)]

for row in range(n):
    temp = input().split(' ')
    for col in range(n):
        matrix[row][col] = temp[col]
flag = True
for i in range(n):
    for j in range(n):
        if int(matrix[i][j]) != int(matrix[j][i]):
            flag = False

if flag == True:
    print('YES')
else:
    print('NO')