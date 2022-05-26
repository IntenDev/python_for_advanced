num = int(input())
fridge = []
word = 'anton'
cnt= []
result = ''
for i in range(num):
    fridge.append(input())

for j in range(num):

    for y in range(len(fridge[j])):

        if len(result) < 5:
            if fridge[j][y] in word[len(result)]:
                result += fridge[j][y]
        else:
            break
    if result == word:
        cnt.append(j + 1)
        result = ''
    else:
        result = ''
print(*cnt)