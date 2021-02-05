from fibonacci import *


while True:
    data = input()
    if data == "Stop":
        break
    data = data.split()
    command = data[0]
    num = int(data[-1])
    if command == "Create":
        f_sequence = fibonacci_sequence(num)
        print(*[str(n) for n in f_sequence])
    elif command == "Locate":
        if not check_num_in_fibonacci_sequence(f_sequence, num):
            print(f"The number {num} is not in the sequence")
        else:
            index = check_num_in_fibonacci_sequence(f_sequence, num)
            print(f"The number - {num} is at index {index}")
