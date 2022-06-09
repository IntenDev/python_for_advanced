str1, num = input(), int(input())

def chunked(n, string):
    list1 = string.split(' ')
    result = []

    for i in range(0, len(list1), n):
        result.append(list1[i:i+n])

    return result

print(chunked(num, str1))