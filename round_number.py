def closest_mod_5(x):
    while x % 5 !=0:
        x += 1
        if x % 5 == 0:
            return x

    return "I don't know :("

num = int(input())

print(closest_mod_5(num))