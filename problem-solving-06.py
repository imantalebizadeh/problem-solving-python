def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(3)) -> 2


def reverse_name(name):
    reversed_name = ""

    for char in name:
        reversed_name = char + reversed_name

    return reversed_name


# print(reverse_name("Iman")) -> "namI"
