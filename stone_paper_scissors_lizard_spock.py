timur = input().lower()
ruslan = input().lower()
words = ['ножницы', 'бумага', 'камень', 'ящерица', 'спок']

if timur == words[0] and ruslan == words[1] or timur == words[0] and ruslan == words[3]:
    print('Тимур')
elif ruslan == words[0] and timur == words[1] or ruslan == words[0] and timur == words[3]:
    print('Руслан')
elif timur == words[1] and ruslan == words[2] or ruslan == words[0] and ruslan == words[4]:
    print('Тимур')
elif ruslan == words[1] and timur == words[2] or ruslan == words[1] and timur == words[4]:
    print('Руслан')
elif timur == words[2] and ruslan == words[3] or timur == words[2] and ruslan == words[0]:
    print('Тимур')
elif ruslan == words[2] and timur == words[3] or ruslan == words[2] and timur == words[0]:
    print('Руслан')
elif timur == words[3] and ruslan == words[4] or timur == words[3] and ruslan == words[1]:
    print('Тимур')
elif ruslan == words[3] and timur == words[4] or ruslan == words[3] and timur == words[1]:
    print('Руслан')
elif timur == words[4] and ruslan == words[0] or timur == words[4] and ruslan == words[2]:
    print('Тимур')
elif ruslan == words[4] and timur == words[0] or ruslan == words[4] and timur == words[2]:
    print('Руслан')

else:
    print('ничья')