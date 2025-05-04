import math


def func(x):
    if x > 0 and x <= 1:
        return x
    else:
        return 1 + math.exp(-x)


print(func(1))  # 1
print(func(2))  # 1.1353352832366128


def absolute(x):
    if x < 0:
        return -x
    return x


print(absolute(-1))  # 1
print(absolute(1))  # 1
print(absolute(0))  # 0
