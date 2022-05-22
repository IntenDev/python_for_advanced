num = int(input())
nums = []
flag = False
for i in range(num):
    nums.append(int(input()))
prod_num = int(input())

for j in range(len(nums)):
    for y in range(len(nums)):
        if j != y and nums[j] * nums[y] == prod_num:
            flag = True
if flag:
    print('ДА')
else:
    print('НЕТ')