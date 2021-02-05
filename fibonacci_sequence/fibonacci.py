def fibonacci_sequence(num):
    result = [0, 1]
    for i in range(2, num):
        next_num = result[i - 2] + result[i - 1]
        result.append(next_num)
    return result


def check_num_in_fibonacci_sequence(seq, n):
    for i in range(len(seq)):
        if seq[i] == n:
            return i