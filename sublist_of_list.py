
list1 = input().split(" ")
temp_list = []
result = [[]]
for i in range(len(list1)):
    for j in range(len(list1)):
        temp_list = list1[j:i+j+1]
        if len(temp_list) == i+1:
            result.append(temp_list)

print(result)