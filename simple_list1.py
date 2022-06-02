n = int(input())
list1 =[]
for i in range(n):
    list1.append([])
    for j in range(1, n+1):
        list1[i].append(j)
    print(list1[i])