def func_b(a, c, d):
    return (a // c) + d


print(func_b(10, 3, 5))
# 10//3+5 = 8


def func_y(b, x, a):
    return (b * x) // (a // x)


print(func_y(10, 3, 5))
# 10*3//(5//3) = 18


def calculate_circle_area(radius):
    PI = 3.14
    return PI * radius**2


print(calculate_circle_area(5))
# 3.14 * 5 * 5 = 78.5
