all_dot = int(input())
first_quot = 0
second_quot = 0
third_quot = 0
fourth_quot = 0
for i in range(all_dot):
    coord = input().split(' ')
    if int(coord[0]) > 0 and int(coord[1]) > 0:
        first_quot += 1
    elif int(coord[0]) > 0 and int(coord[1]) < 0:
        fourth_quot += 1
    elif int(coord[0]) < 0 and int(coord[1]) < 0:
        third_quot += 1
    elif int(coord[0]) < 0 and int(coord[1]) > 0:
        second_quot += 1

print(r'Первая четверть:', first_quot)
print('Вторая четверть:', second_quot)
print('Третья четверть:', third_quot)
print('Четвертая четверть:', fourth_quot)
