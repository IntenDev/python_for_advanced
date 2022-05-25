timur = input().lower()
ruslan = input().lower()
if timur == 'бумага' and ruslan == 'ножницы' or timur == 'камень' and ruslan == 'бумага' or timur == 'ножницы' and ruslan == 'камень':
    print('Руслан')
elif timur == 'ножницы' and ruslan == 'бумага' or timur == 'бумага' and ruslan == 'камень' or timur == 'камень' and ruslan == 'ножницы':
    print('Тимур')
else:
    print('ничья')