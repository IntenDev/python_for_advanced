from math import ceil

list1 = input().split(" ")

L = int(list1[0])
W = int(list1[1])
H = int(list1[2])

print(ceil(((L*H + W*H)*2)/16))