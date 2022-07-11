digit_chess = [8, 7, 6, 5, 4, 3, 2, 1]
char_chess = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
place = input()
matrix = [['.'] * 8 for _ in range(8)]
ch = char_chess.index(place[0])
dg = digit_chess.index(int(place[1]))
# Отмечаем местонахождение коня
matrix[dg][ch] = 'N'
desk = 8
# Заполняем матрицу
for i in range(desk):
    for j in range(desk):
        if (i-dg)**2 + (j-ch)**2 == 5:
            matrix[i][j] = '*'
# распечататка матрицы
for c in range(desk):
    for r in range(desk):
        print(matrix[c][r],  end=' ')
    print()