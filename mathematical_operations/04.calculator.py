from math_operations import *


num_1, operator, num_2 = input().split()
num_1 = float(num_1)
num_2 = int(num_2)

if operator == "+":
    result = add(num_1, num_2)
elif operator == "-":
    result = subtract(num_1 - num_2)
elif operator == "*":
    result = multiply(num_1, num_2)
elif operator == "/":
    result = divide(num_1, num_2)
elif operator == "^":
    result = power(num_1, num_2)
else:
    Exception("Error operator")
print(result)