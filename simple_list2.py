num = int(input())
list1 =[]
CNT = 1
for i in range(num):
    list1.append([])
    for j in range(CNT):
        list1[i].append(j+1)
    CNT += 1
    print(list1[i])
