num = int(input())
matrix = [['']*num for _ in range(num)]
result = -10000
up_quarter = 0
right_quarter = 0
left_quarter = 0
down_quarter = 0
for row in range(num):
    temp = input().split(' ')
    for col in range(num):
        matrix[row][col] = temp[col]

for i in range(num):
    for j in range(num):
        if i < j and i < num - 1 -j:
            up_quarter += int(matrix[i][j])
        if i < j and i > num-1-j:
            right_quarter += int(matrix[i][j])
        if i > j and i > num - 1 - j:
            down_quarter += int(matrix[i][j])
        if i > j and i < num - 1 - j:
            left_quarter += int(matrix[i][j])

print('Верхняя четверть:', up_quarter)
print('Правая четверть:', right_quarter)
print('Нижняя четверть:', down_quarter)
print('Левая четверть:', left_quarter)
