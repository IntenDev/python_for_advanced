n = int(input())
m = int(input())
matrix = [[' '] * m for _ in range(n)]
elements = input().split(' ')
count = 0
temp = []
value = [0, 0]

for i in range(n):
    for j in range(m):
        matrix[i][j] = elements[count]

        if count > 0 and elements[count] > elements[count-1] and elements[count] not in temp:
            value[0] = i
            value[1] = j
        temp.append(elements[count])
        count += 1

print(*value, end=' ')
