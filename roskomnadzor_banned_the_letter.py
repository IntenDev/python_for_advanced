word = input() + ' запретил букву'
letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
result = word
ch = []
for i in range(len(letters)):
    if letters[i] in result:
        print(result + ' ' + letters[i])
        ch.append(letters[i])
        result = result.replace(ch[-1], '').strip()
        result = result.replace('  ', ' ').strip()

