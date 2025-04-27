import math as mt


def func_a(x, y):
    return -(x / y) * mt.log(x / y)


# print(func_a(10, 2))
# result: -8.047189562170502


def func_b(x):
    return 1 / 1 + mt.exp(-x)


# print(func_b(10))
# result: 1.0000453999297625


def func_c(x):
    return mt.exp(x) / mt.exp(mt.pow(x, 2))


# print(func_c(5))
# result: 2.0611536224385575e-09


def func_d(x, y, y1):
    return (1 / x) * (y - y1)


# print(func_d(10, 20, 3))
# result: 1.7000000000000002


def func_e(x):
    return mt.sqrt(x * mt.log(x))


# print(func_e(10))
# result: 4.798525912188081
