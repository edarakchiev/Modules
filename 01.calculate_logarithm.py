from math import log


def calculate_log(num, base):
    if base == "natural":
        return f"{log(num):.2f}"
    base = int(base)
    return f"{log(num, base):.2f}"


number = int(input())
b = input()
print(calculate_log(number, b))