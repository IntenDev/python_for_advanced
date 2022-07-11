n = int(input(''))
numbers = ['0']
result, row, col, col_end, flag = 0, 0, 0, 0, True
for c in range(n):
    temp = input().split(' ')
    for r in range(n):
        if temp[r] not in numbers:
            row += int(temp[r])
            numbers.append(temp[r])
            if r == n - 1:
                col_end += int(temp[r])
        else:
            flag = False
        if r == 0:
            col += int(temp[r])
    if c == 0:
        result = row
    if row != result:
        flag = False
    row = 0
if col_end != result:
    flag = False
if col != result:
    flag = False
if flag == True:
    print("YES")
else:
    print('NO')
