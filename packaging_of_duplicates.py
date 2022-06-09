str1 = input().split(" ")
my_list =[]
temp_list = []
for i in range(len(str1)):

    if len(temp_list) == 0 or str1[i] == temp_list[0]:
        temp_list.append(str1[i])
    else:
        my_list.append(temp_list)
        temp_list = []
        temp_list.append(str1[i])
my_list.append(temp_list)
print(my_list)